#!/usr/bin/env python3
import argparse
import json
import pathlib
from datetime import datetime, date, timezone

import yaml
from jsonschema import Draft202012Validator


def load_yaml(path: pathlib.Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def load_json(path: pathlib.Path):
    return json.loads(path.read_text(encoding="utf-8"))


def parse_date(val):
    if not val or not isinstance(val, str):
        return None
    try:
        return datetime.fromisoformat(val).date()
    except Exception:
        try:
            return date.fromisoformat(val)
        except Exception:
            return None


def get_branch(data):
    for path in [
        ("final_group_outcome", "branch"),
        ("branch_binding", "branch"),
        ("DecisionLedger_hint", "branch_candidate"),
        ("runtime_event", "expected_branch"),
        ("evaluation_context", "intended_branch"),
        ("consistency_repair_result", "action"),
    ]:
        cur = data
        ok = True
        for p in path:
            if isinstance(cur, dict) and p in cur:
                cur = cur[p]
            else:
                ok = False
                break
        if ok and isinstance(cur, str):
            return cur
    return None


def get_followup_branch(data):
    for path in [
        ("followup_branch",),
        ("response_action",),
        ("DecisionLedger_hint", "branch_candidate"),
        ("runtime_event", "expected_branch"),
        ("consistency_repair_result", "action"),
    ]:
        cur = data
        ok = True
        for p in path:
            if isinstance(cur, dict) and p in cur:
                cur = cur[p]
            else:
                ok = False
                break
        if ok and isinstance(cur, str):
            return cur
    return None


def get_risk_tier(data):
    return data.get("evaluation_context", {}).get("risk_tier")


def get_validation_status(data):
    return data.get("evaluation_context", {}).get("validation_status")


def vote_total(vote_summary):
    if not isinstance(vote_summary, dict):
        return None
    total = 0
    seen = False
    for key in ["approve", "reject", "abstain", "defer"]:
        if key in vote_summary and isinstance(vote_summary[key], int):
            total += vote_summary[key]
            seen = True
    return total if seen else None


def premise_present_count(premise_results):
    if not isinstance(premise_results, list) or not premise_results:
        return None
    counts = []
    for item in premise_results:
        if isinstance(item, dict):
            total = 0
            seen = False
            for key in ["yes", "no", "abstain"]:
                if key in item and isinstance(item[key], int):
                    total += item[key]
                    seen = True
            if seen:
                counts.append(total)
    return max(counts) if counts else None


def failed_training_premise(premise_results):
    if not isinstance(premise_results, list):
        return False
    for item in premise_results:
        if isinstance(item, dict) and item.get("premise_ref") == "operator_training_ready":
            yes = item.get("yes", 0) or 0
            no = item.get("no", 0) or 0
            if no > yes:
                return True
    return False


def has_failed_premise(premise_results):
    if not isinstance(premise_results, list):
        return False
    for item in premise_results:
        if isinstance(item, dict):
            yes = item.get("yes", 0) or 0
            no = item.get("no", 0) or 0
            if no > yes:
                return True
    return False


def contested_conclusion(data):
    if data.get("contested_conclusion") is True:
        return True
    vt = data.get("vote_summary")
    if isinstance(vt, dict):
        return (vt.get("approve", 0) or 0) > 0 and (vt.get("reject", 0) or 0) > 0
    return False


def add_finding(findings, rule_id, severity, message, path=""):
    findings.append({"rule_id": rule_id, "severity": severity, "message": message, "path": path})


def load_schema_validators(package_root: pathlib.Path):
    schema_dir = package_root / "08_institutional_annex" / "json_schema"
    schema_map = {
        "epistemic_justification_packet": schema_dir / "epistemic_justification_packet.schema.json",
        "aggregation_rule_profile": schema_dir / "aggregation_rule_profile.schema.json",
        "minority_report_packet": schema_dir / "minority_report_packet.schema.json",
        "lifecycle_gate_packet": schema_dir / "lifecycle_gate_packet.schema.json",
        "ops_feedback_event": schema_dir / "ops_feedback_event.schema.json",
        "human_oversight_packet": schema_dir / "human_oversight_packet.schema.json",
    }
    return {k: Draft202012Validator(load_json(v)) for k, v in schema_map.items()}


def validate_structures(data, validators, findings):
    for key, validator in validators.items():
        if key in data:
            errs = sorted(validator.iter_errors(data[key]), key=lambda e: e.path)
            for err in errs:
                add_finding(findings, f"SCHEMA-{key}", "error", err.message, path="/" + "/".join(map(str, err.path)))


def apply_rules(data, validators):
    findings = []
    validate_structures(data, validators, findings)
    branch = get_branch(data)
    risk = get_risk_tier(data)
    eval_date = parse_date(data.get("evaluation_context", {}).get("evaluation_date"))

    ejp = data.get("epistemic_justification_packet")
    if isinstance(ejp, dict):
        swp = ejp.get("speaker_warrant_profile")
        if branch == "execute" and risk in {"high", "critical"} and swp in {"domain_expert", "external_authority"}:
            if not isinstance(ejp.get("expertise_scope"), dict) or not ejp.get("expertise_scope", {}).get("domain_ref"):
                add_finding(findings, "KCI-T1-001", "error", "high-risk execute の expert warrant に expertise_scope.domain_ref が無い。", "/epistemic_justification_packet/expertise_scope")
        if branch == "execute" and risk in {"high", "critical"} and ejp.get("trust_channel") == "public_claim":
            add_finding(findings, "KCI-T1-002", "error", "public_claim 単独を high-risk execute basis にしている。", "/epistemic_justification_packet/trust_channel")
        stale_after = parse_date(ejp.get("freshness_window", {}).get("stale_after")) if isinstance(ejp.get("freshness_window"), dict) else None
        if eval_date and stale_after and eval_date > stale_after:
            if ejp.get("epistemic_transfer_status") in {None, "transferable"}:
                add_finding(findings, "KCI-T1-003", "error", "stale な packet が transferable のまま保持されている。", "/epistemic_justification_packet/epistemic_transfer_status")
        dr = ejp.get("defeater_register")
        if isinstance(dr, list) and any(isinstance(d, dict) and d.get("kind") == "conflict_of_interest" for d in dr):
            if not ejp.get("conflict_of_interest_status"):
                add_finding(findings, "KCI-T1-004", "warning", "conflict_of_interest があるのに conflict_of_interest_status が無い。", "/epistemic_justification_packet/conflict_of_interest_status")
        if branch == "execute" and risk in {"high", "critical"} and ejp.get("epistemic_transfer_status") in {"qualified", "stale", "scope_exceeded", "defeated"}:
            if data.get("corroboration_status") not in {"independent_confirmed", "multi_source_confirmed"}:
                add_finding(findings, "KCI-X-001", "error", "qualified/stale testimony で high-risk execute しているのに独立 corroboration が無い。", "/corroboration_status")

    agr = data.get("aggregation_rule_profile")
    fgo = data.get("final_group_outcome")
    if fgo is not None and not isinstance(agr, dict):
        add_finding(findings, "KCI-S1-001", "error", "group outcome があるのに aggregation_rule_profile が無い。", "/aggregation_rule_profile")
    if isinstance(agr, dict):
        minimum_present = agr.get("quorum_rule", {}).get("minimum_present") if isinstance(agr.get("quorum_rule"), dict) else None
        observed = vote_total(data.get("vote_summary"))
        if observed is None:
            observed = premise_present_count(data.get("premise_results"))
        if isinstance(minimum_present, int) and isinstance(observed, int) and observed < minimum_present:
            add_finding(findings, "KCI-S1-002", "error", f"quorum minimum_present={minimum_present} に対して observed_present={observed}。", "/aggregation_rule_profile/quorum_rule/minimum_present")
        if agr.get("minority_report_policy") == "required_when_conclusion_contested" and contested_conclusion(data):
            if "minority_report_packet" not in data:
                add_finding(findings, "KCI-S1-003", "error", "contested conclusion なのに required な minority report が無い。", "/minority_report_packet")
        guard = agr.get("consistency_guard")
        issue = contested_conclusion(data) or has_failed_premise(data.get("premise_results"))
        if guard in {"inconsistency_requires_repair", "all_required_premises_must_pass"} and issue:
            if isinstance(fgo, dict) and fgo.get("branch") == "execute" and "consistency_repair_result" not in data:
                add_finding(findings, "KCI-S1-004", "error", "repair が必要な不整合を repair 無しで execute に直結している。", "/consistency_repair_result")

    lgp = data.get("lifecycle_gate_packet")
    if isinstance(lgp, dict):
        if branch == "execute" and lgp.get("artifact_class") == "baseline" and not lgp.get("baseline_id"):
            add_finding(findings, "KCI-O1-001", "error", "baseline execute に baseline_id が無い。", "/lifecycle_gate_packet/baseline_id")
        if branch == "execute":
            if not lgp.get("entry_criteria") or not lgp.get("exit_criteria") or not lgp.get("responsible_role"):
                add_finding(findings, "KCI-O1-002", "error", "managed execute に必要な gate 条件または responsible_role が欠けている。", "/lifecycle_gate_packet")
        if branch == "execute" and risk in {"high", "critical"} and get_validation_status(data) == "pending":
            if not data.get("exception_basis"):
                add_finding(findings, "KCI-O1-003", "error", "validation pending の high-risk execute に exception_basis が無い。", "/exception_basis")

    ofe = data.get("ops_feedback_event")
    if isinstance(ofe, dict) and ofe.get("triggers_reopen") is True:
        fb = get_followup_branch(data)
        if fb not in {"rollback", "reopen", "escalate", "hold", "revalidate"}:
            add_finding(findings, "KCI-O1-004", "error", "reopen trigger があるのに follow-up path が不明または不適切。", "/ops_feedback_event/triggers_reopen")

    hop = data.get("human_oversight_packet")
    if isinstance(hop, dict):
        roles = hop.get("human_roles") if isinstance(hop.get("human_roles"), list) else []
        rights = hop.get("override_rights") if isinstance(hop.get("override_rights"), dict) else {}
        scopes = hop.get("explanation_scope_by_role") if isinstance(hop.get("explanation_scope_by_role"), dict) else {}
        if any(role not in rights or role not in scopes for role in roles):
            add_finding(findings, "KCI-H1-001", "error", "human_roles の全 role に override_rights と explanation_scope_by_role が割り当てられていない。", "/human_oversight_packet")
        if hop.get("training_readiness") in {"incomplete", "retraining_required"} and branch == "execute" and not data.get("supervisory_exception"):
            add_finding(findings, "KCI-H1-002", "error", "training incomplete/retraining_required のまま execute している。", "/human_oversight_packet/training_readiness")
        manual_fb = hop.get("manual_fallback") if isinstance(hop.get("manual_fallback"), dict) else {}
        if risk in {"high", "critical"} and manual_fb.get("available") is False and not data.get("no_fallback_justification"):
            add_finding(findings, "KCI-H1-003", "warning", "high-risk なのに fallback 不在の justification が無い。", "/no_fallback_justification")
        if hop.get("operator_acceptance") == "not_ready" and branch == "execute":
            if data.get("evaluation_context", {}).get("deployment_mode") != "shadow":
                add_finding(findings, "KCI-H1-004", "error", "operator not_ready の execute が shadow mode でない。", "/evaluation_context/deployment_mode")

    if branch == "execute" and (failed_training_premise(data.get("premise_results")) or (isinstance(hop, dict) and hop.get("training_readiness") in {"incomplete", "retraining_required"})):
        add_finding(findings, "KCI-X-002", "error", "training failure と execute が共存している。", "/premise_results")

    return findings


def outcome_from_findings(findings):
    severities = {f["severity"] for f in findings}
    if "error" in severities:
        return "fail"
    if "warning" in severities:
        return "warn"
    return "pass"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--suite", default="09_conformance_suite/institutional_conformance_test_suite_v1.yaml")
    parser.add_argument("--output", default="09_conformance_suite/validation_report_v1.yaml")
    args = parser.parse_args()

    package_root = pathlib.Path(__file__).resolve().parents[2]
    suite_path = package_root / args.suite
    output_path = package_root / args.output

    suite = load_yaml(suite_path)
    validators = load_schema_validators(package_root)

    case_results = []
    counts = {"pass": 0, "warn": 0, "fail": 0}
    mismatches = 0

    for case in suite["cases"]:
        input_path = (suite_path.parent / case["input_file"]).resolve()
        data = load_yaml(input_path)
        findings = apply_rules(data, validators)
        actual_outcome = outcome_from_findings(findings)
        actual_rule_hits = sorted([f["rule_id"] for f in findings if not f["rule_id"].startswith("SCHEMA-")])
        expected_rule_hits = sorted(case["expected_rule_hits"])
        matched = actual_outcome == case["expected_outcome"] and actual_rule_hits == expected_rule_hits
        if not matched:
            mismatches += 1
        counts[actual_outcome] += 1
        case_results.append(
            {
                "test_id": case["test_id"],
                "profile": case["profile"],
                "input_file": case["input_file"],
                "actual_outcome": actual_outcome,
                "expected_outcome": case["expected_outcome"],
                "actual_rule_hits": actual_rule_hits,
                "expected_rule_hits": expected_rule_hits,
                "matched_expectation": matched,
                "findings": findings,
            }
        )

    overall = "pass" if mismatches == 0 else "fail"
    report = {
        "suite_ref": args.suite,
        "generated_on": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "overall_result": overall,
        "summary": {
            "total_cases": len(case_results),
            "pass": counts["pass"],
            "warn": counts["warn"],
            "fail": counts["fail"],
            "expectation_mismatches": mismatches,
        },
        "case_results": case_results,
    }
    output_path.write_text(yaml.safe_dump(report, allow_unicode=True, sort_keys=False, width=1000), encoding="utf-8")
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()

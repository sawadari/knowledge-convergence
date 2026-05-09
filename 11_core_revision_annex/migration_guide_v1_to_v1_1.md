# v1 から v1.1 への移行ガイド

## 1. 既存実装を壊さない最小移行

既存の `K=(G,C,E,V,R,H)`、`decision_outcome`、`hold_packet` はそのまま使える。まず、次の optional packet を追加する。

```text
domain_validity_packet_minimum
agent_execution_envelope_minimum
meaningful_human_oversight_packet_minimum
organization_topology_packet_minimum
convergence_metrics_packet_minimum
```

## 2. 高影響 execute の移行ルール

高影響、対外コミット、安全関連、規制関連、AI/agent実行を含む branch では、次を要求する。

```text
C_e = true
C_g = true or governance_entry_state = eligible
C_d = true or explicit exception_basis
meaningful_human_oversight = meaningful or justified exception
agent_execution_envelope valid when agent executes
```

## 3. SEシステムでの移行

SEシステムでは、`domain_validity_packet` を `engineering_validity_packet` として扱う。

最低限、次を接続する。

```text
Requirement -> Verification
Need / Mission -> Validation Scenario
Decision -> Rationale / Evidence / Reopen Condition
Agent Execution -> Authority Envelope / Audit / Rollback
Organization Role -> Decision Right / Expertise Scope / Review Capacity
```

## 4. 失敗しやすい移行

- 承認済みだから domain_validity=true とする。
- テスト通過を Validation 通過とみなす。
- human-in-the-loop と書くだけで meaningful oversight とする。
- agent の owner_role と accountable_role を分けない。
- 収束スコア平均で blocker を隠す。

# 実装クイックスタート

## 1. まず決めること
自分の実装がどの準拠レベルを目指すかを決めます。

- 説明可能な知識候補を扱いたいだけなら `KC-E1`
- 承認や責任まで扱いたいなら `KC-G1`
- 自動化や委任を扱いたいなら `KC-D1`
- 監査や差戻しを強く扱いたいなら `KC-A1`

対応: `conformance_profiles_public_v1.yaml`

## 2. 最小データ形を採用する
`canonical_public_data_contract_v1.yaml` に従って、最低でも次を作ります。

- KnowledgeState
- UpdateRequest
- DecisionOutcome
- HoldPacket
- HistoryEvent

## 3. 最小の評価流れ
1. `G/C/E` を作る
2. Epistemic 評価を返す
3. 実行判断が必要なら `V/R` を追加する
4. Governance 評価を返す
5. `execute / hold / reject / escalate / rollback` のいずれかを決める
6. 履歴 `H` を残す

## 4. 最低限の責務分離
- GraphLint: 構造・文脈・根拠の検査
- DecisionLedger: 価値・責任・承認・branch 決定
- GraphEngine: 状態遷移と履歴保存

この3つをコード上で別モジュールに分けると実装が崩れにくくなります。

## 5. 最初に実装するとよいバリデーション
- claim に relation/constraint が無いなら KC-E1 不合格
- scope が無いなら KC-E1 不合格
- evidence_ref も evidence_status も無いなら KC-E1 不合格
- V/R が無いのに governance true を返したら KC-G1 不合格
- authority_basis 無しで execute したら KC-G1 不合格
- AI/agent を Ex に含むのに D が無ければ KC-D1 不合格

## 6. 具体例を見る
- `examples/material_change_hold.yaml`
- `examples/policy_update_execute.yaml`
- `examples/delegated_postcheck_rollback.yaml`

## 7. 実務での導入順
### 小さく始める
1. `KC-E1`
2. `KC-G1`
3. 必要になってから `KC-D1`

### 最初から避けた方がよいこと
- いきなり weighted quorum や大型 forum 競合を実装する
- null だけで missingness を表す
- AI 実行を責任束縛より先に入れる
- hold をエラー扱いにして失う

## 8. 理論根拠を確認したいとき
- 概念面: `concepts_public_spec_v1.yaml` → `concepts_core_v1.yaml`
- 形式面: `formalization_public_spec_v1.yaml` → `formalization_core_v1.yaml`

## 9. annex を足したくなったら
公開仕様だけでは足りず、しかし raw supplement は重すぎると感じたら `../06_public_annex/` を見ます。

- authority / delegation / weighted quorum: `public_annex_concepts_v1.yaml`, `public_annex_formalization_v1.yaml`
- hold reason の関係語彙: `public_annex_concepts_v1.yaml`, `public_annex_formalization_v1.yaml`
- 監査ログ / redaction / bounded summary: `public_annex_crosswalk_v1.yaml`

## 10. 言語解釈と数学拡張が必要になったら
次のような問題が出たら `foundational` 系を採用します。

- 報告伝聞、推量、曖昧語をそのまま claim 化すると誤る
- H2 を「衝突あり」の一語で潰したくない
- 多基準比較で単一スコアに落とせない
- approval の有効期限や hold の失効条件を機械検査したい
- 由来追跡と rollback 可能性を強くしたい

入口:
- プロファイル: `foundational_extension_profiles_v1.yaml`
- データ追加契約: `foundational_contract_addendum_v1.yaml`
- 詳細仕様: `../07_foundational_annex/00_start_here_foundational_annex.md`

### 推奨導入順
1. `KC-L1` 発話解釈
2. `KC-M1` 競合意味論
3. `KC-M2` 多基準判断
4. `KC-M3` 由来・時相保証

### 典型的な接続位置
- 上流入力の直後: `utterance_interpretation_envelope`
- GraphLint の拡張: `ambiguity_profile`, `argument_graph_packet`
- DecisionLedger の拡張: `measurement_profile`, `outranking_profile`
- GraphEngine / Audit の拡張: `provenance_trace_packet`, `temporal_guard_packet`

## 11. 集団判断と運用保証が必要になったら
次のような問題が出たら `institutional` 系を採用します。

- 誰の証言や専門判断を、どこまで信じるかを source quality 以上に扱いたい
- 複数レビューの結果を合議として整合的に残したい
- execute / rollback を gate, baseline, runbook, training と結び付けたい
- 現場の人が停止・引継ぎ・手動代替できる条件を明示したい

入口:
- プロファイル: `institutional_extension_profiles_v1.yaml`
- データ追加契約: `institutional_contract_addendum_v1.yaml`
- 詳細仕様: `../08_institutional_annex/00_start_here_institutional_annex.md`

### 推奨導入順
1. `KC-T1` 証言・正当化
2. `KC-S1` 合議・集約
3. `KC-O1` ライフサイクル運用
4. `KC-H1` 人間中心監督

### 典型的な接続位置
- GraphLint の拡張: `epistemic_justification_packet`, `defeater_register`
- DecisionLedger の拡張: `aggregation_rule_profile`, `minority_report_packet`
- GraphEngine / Ops の拡張: `lifecycle_gate_packet`, `ops_feedback_event`
- HMI / Console の拡張: `human_oversight_packet`, `manual_fallback`

## 12. 導入順の目安
- 入力誤読が多いなら foundational を先に入れる
- 証言や専門家レビューが中心なら `KC-T1` を先に入れる
- 承認委員会や複数レビューが中心なら `KC-S1` を先に入れる
- 実運用・保守・障害再開が重いなら `KC-O1` と `KC-H1` を続けて入れる


## 13. 制度運用 annex を実装したら検査も入れる
`KC-T1 / KC-S1 / KC-O1 / KC-H1` を採用したら、schema だけでなく意味規則も検査します。

入口:
- `../09_conformance_suite/00_start_here_conformance_suite.md`
- `../09_conformance_suite/institutional_validation_rulebook_v1.yaml`
- `../09_conformance_suite/institutional_conformance_matrix_v1.yaml`
- `../09_conformance_suite/institutional_conformance_test_suite_v1.yaml`
- `../09_conformance_suite/validation_report_v1.yaml`

最低限の見どころ:
- high-risk execute に expert label だけを使っていないか
- contested conclusion に minority report や repair が残っているか
- execute が baseline / gate / validation 状態と結び付いているか
- training incomplete や no fallback を lawful に止められるか

実装チームでは、`rule_id` 単位で CI・review gate・release gate へ結び付けると崩れにくくなります。


---

## v1.1 追加実装順序

v1.1 で最小実装を拡張する場合、既存の `K=(G,C,E,V,R,H)` と `decision_outcome` を維持したまま、次を追加する。

1. `domain_validity_packet_minimum`: 対象ドメインで使ってよいかを判定する。
2. `agent_execution_envelope_minimum`: AI/agent 実行の権限・監査・停止・rollback を定義する。
3. `meaningful_human_oversight_packet_minimum`: 人間が意味ある介入をできるかを定義する。
4. `organization_topology_packet_minimum`: 組織構造・専門性・意思決定権・review capacity を定義する。
5. `convergence_metrics_packet_minimum`: 収束状態を多次元に計量する。

高影響 execute では、平均点ではなく blocker-preserving なゲートで判定する。

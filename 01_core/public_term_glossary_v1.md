# 公開用用語集

## Knowledge
判断・説明・見直し・実行可否判定に耐えるよう、構造・文脈・根拠・必要に応じて価値と責任が束縛された状態。

対応: `concepts_core_v1.yaml::central_definitions.knowledge`

## Convergence
唯一の正解への押し込みではなく、所与の目的と責任条件の下で、判断可能・説明可能・差戻し可能な状態へ到達すること。

対応: `concepts_core_v1.yaml::central_definitions.convergence`

## Epistemic Convergence
主張の構造、文脈境界、根拠接続、主要矛盾・曖昧性管理、説明経路が成立している状態。

対応: `concepts_core_v1.yaml::central_definitions.epistemic_governance_connection`

## Governance Convergence
決定対象、採択基準・許容リスク、責任割当、保留条件、影響分類が束縛され、実行分岐を選べる状態。

対応: `concepts_core_v1.yaml::central_definitions.epistemic_governance_connection`

## Knowledge State
知識収束判定のための拡張状態。公開仕様では `K = (G, C, E, V, R, H)` を採る。

対応: `formalization_core_v1.yaml::knowledge_state`

## G / C / E / V / R / H
- G: 構造化グラフ
- C: 文脈
- E: 根拠集合
- V: 価値基準・許容リスク・優先関係・棄却条件
- R: 承認主体・実行主体・結果責任主体・エスカレーション・委任範囲
- H: 履歴

## Hold
失敗ではなく、未成立状態を reason code と解消パケット付きで保つ正規状態。

対応: `formalization_core_v1.yaml::hold_reason_model`

## Hold Reason
公開仕様では H1〜H6 を最小集合として使う。
- H1: epistemic_gap
- H2: epistemic_conflict
- H3: governance_unbound
- H4: approval_pending
- H5: risk_excess
- H6: policy_block

## Update Operator
主体が差分要求を、適用中の政策・統治文脈の下で知識状態へ適用する型付き更新作用素。  
表記は `U_a : (K, Δ, Π) -> (K', h, o)`。

## Decision Outcome
`execute / hold / reject / escalate / rollback` のいずれかの branch を選び、その理由と評価状態を残した決定結果。

## Approval Structure
複数承認主体を単なる集合ではなく、mode・必須承認・proxy・quorum・fallback・validity・SoD を持つ構造として表したもの。

## Delegation Policy
自動化主体や委任主体が、どの範囲までどの条件で動けるかを規定する policy。公開仕様では `D = (T, G, X, E_req, F, A)` を使う。

## GraphLint / DecisionLedger / GraphEngine
- GraphLint: 構造・文脈・根拠・矛盾・曖昧性検査
- DecisionLedger: 価値・責任・承認・branch 決定
- GraphEngine: 状態遷移と履歴永続化


---

## v1.1 追加用語

### ドメイン妥当性収束 / domain validity convergence
認識として説明でき、統治上実行可能な知識状態が、対象ドメインの成功条件・検証条件・運用条件へ接続され、そのドメインで使ってよいかを判定できる状態。

### 工学的妥当性収束 / engineering validity convergence
SEシステムにおける domain validity convergence の具体化。要求、設計、Verification、Validation、運用フィードバック、人間・組織能力へ接続される。

### 意味ある人間監督 / meaningful human oversight
人間が形式的に介在するだけでなく、説明を理解し、止める権限を持ち、介入する時間的余裕があり、必要な訓練・代替経路・エスカレーション経路を持つ状態。

### エージェント実行包絡 / agent execution envelope
AI/agent が実行主体になる場合に必要な、権限、入出力範囲、ツール範囲、監査義務、停止条件、rollback、所有者、結果責任の束。

### 組織トポロジー / organization topology
組織ノード、役割、意思決定権、専門性、責任範囲、レビュー能力、サプライヤー境界、エスカレーション経路を含む構造。

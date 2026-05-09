# 基礎発展 annex 導入ロードマップ

## Phase 1: 上流の誤読を止める
対象:
- 自然言語入力を直接 claim 化している実装
- 伝聞・推量・曖昧語の取り扱いが不安定な実装

採用:
- `KC-L1`
- `utterance_interpretation_envelope`
- `ambiguity_profile`

成果:
- 「誰が言ったか」
- 「どの程度コミットしているか」
- 「何がまだ曖昧か」
を claim へ潰さず残せる。

## Phase 2: H2 を粗い衝突フラグから脱却させる
対象:
- conflicting evidence が多い
- 説明責任が重い
- support / rebut / undercut を区別したい

採用:
- `KC-M1`
- `argument_graph_packet`
- `support_status_4`

成果:
- open conflict と lack of information を分離できる。
- H2 の説明に argument edge を添えられる。

## Phase 3: V を単一スコアから守る
対象:
- criteria が複数
- veto がある
- 比較不能を lawful に残したい

採用:
- `KC-M2`
- `measurement_profile`
- `outranking_profile`

成果:
- outranks / indifferent / incomparable / vetoed を保持できる。
- 点数の見かけの精密さに引きずられにくくなる。

## Phase 4: 監査と rollback を時間まで含めて閉じる
対象:
- approval 失効事故がある
- hold の期限管理が必要
- lineage を強く追いたい

採用:
- `KC-M3`
- `provenance_trace_packet`
- `temporal_guard_packet`

成果:
- expired approval を current basis から外せる。
- rollback と reopen を由来依存で追跡できる。

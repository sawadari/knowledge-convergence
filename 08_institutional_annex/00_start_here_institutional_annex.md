# 制度運用発展 annex の入口

`08_institutional_annex/` は、知識収束学を **正当化された証言・合議・運用ライフサイクル・人間中心監督** の方向へ発展させるための annex です。

## 位置づけ
- **最優先の正本**: `01_core/`
- **公開補助 annex**: `06_public_annex/`
- **基礎発展 annex**: `07_foundational_annex/`
- **制度運用発展 annex**: `08_institutional_annex/`
- **raw supplement**: `02_supplements/`

つまり、公開導入では **core → public annex → foundational annex → institutional annex** の順で読む想定です。

## この annex が足すもの
### 認識論
- epistemic justification packet
- speaker warrant / expertise scope / trust channel
- defeater register / conflict of interest / staleness
- testimony から support への transfer 条件

### 合議設計
- aggregation rule profile
- premise-based / conclusion-based distinction
- quorum / weight basis / consistency guard
- minority report / consistency repair / group decision trace

### システム工学・運用工学
- lifecycle gate packet
- baseline / artifact class / entry-exit criteria
- verification / validation / transition package
- ops feedback event / incident-to-reopen loop

### HCI / 人間中心運用
- human oversight packet
- role-scoped explanation
- override / stop rights / escalation path
- cognitive load budget / training readiness / operator acceptance / manual fallback

## 最初に読む順番
1. `institutional_crosswalk_v1.yaml`
2. `../01_core/institutional_extension_profiles_v1.yaml`
3. `epistemic_justification_annex_v1.yaml`
4. `collective_judgment_annex_v1.yaml`
5. `systems_lifecycle_annex_v1.yaml`
6. `human_centered_operations_annex_v1.yaml`
7. `examples/`
8. `json_schema/`
9. `institutional_open_points_v1.yaml`
10. `../09_conformance_suite/00_start_here_conformance_suite.md`

## 規範性の考え方
この annex は `01_core/` と `07_foundational_annex/` を上書きしません。  
ただし、`institutional_role: recommended_institutional_extension` の項目は、**高説明責任実装・組織運用・公開審査・将来の v2 準備** のために採用を推奨します。

## どういうときに読むか
- 証言・専門家レビュー・監査済み記録の扱いが重要
- 複数レビューや委員会判断を一貫した形で残したい
- execute / rollback を運用 gate や baseline に結び付けたい
- 現場の人の停止権・説明要件・訓練状態を状態として管理したい


## 検査まで進めたいとき
この annex で増やした packet は、次段の `../09_conformance_suite/` で **schema + semantic rule + scenario test** として検査できます。  
特に `KC-T1 / KC-S1 / KC-O1 / KC-H1` を実装に入れた後は、`institutional_validation_rulebook_v1.yaml` と `validation_report_v1.yaml` を合わせて見ると導入しやすくなります。


## SEシステム統合 annex との関係

`10_se_system_annex/` は、この institutional annex の `KC-T1 / KC-S1 / KC-O1 / KC-H1` を、システム開発における組織構造・人間系・AIエージェント運用へ適用する応用統合 annex です。

- `KC-T1` は、専門家証言、顧客発話、規格解釈、サプライヤー発言の warrant 管理に使います。
- `KC-S1` は、設計レビュー、変更審査、複数専門家合議、minority report に使います。
- `KC-O1` は、baseline、gate、artifact、Verification / Validation、ops feedback に使います。
- `KC-H1` は、人間の停止権、説明範囲、訓練状態、手動代替、認知負荷管理に使います。

SEシステム統合は、この annex を上書きしません。SEドメインでの追加採用条件として `KC-SE0`〜`KC-SE5` を定義します。

# 基礎発展 annex の入口

`07_foundational_annex/` は、知識収束学を **言語学的な上流解釈** と **数学的な下流評価** の両方向へ発展させるための annex です。

## 位置づけ
- **最優先の正本**: `01_core/`
- **公開補助 annex**: `06_public_annex/`
- **基礎発展 annex**: `07_foundational_annex/`
- **制度運用発展 annex**: `../08_institutional_annex/`
- **raw supplement**: `02_supplements/`

つまり、公開導入では **core → public annex → foundational annex → institutional annex** の順で読む想定です。

## この annex が足すもの
### 上流
- 発話解釈 envelope
- speech act / speaker commitment / evidentiality
- presupposition / deictic anchor / discourse relation
- ambiguity の細分化
- gradable term の threshold profile
- claim_kind typing

### 下流
- four-valued support status
- argument graph と conflict relation taxonomy
- outranking / measurement profile / interval uncertainty
- provenance trace
- temporal guard と validity interval

## 最初に読む順番
1. `foundational_crosswalk_v1.yaml`
2. `../01_core/foundational_extension_profiles_v1.yaml`
3. `foundational_language_annex_v1.yaml`
4. `foundational_mathematical_annex_v1.yaml`
5. `examples/`
6. `json_schema/`
7. `foundational_open_points_v1.yaml`
8. 次段階として `../08_institutional_annex/00_start_here_institutional_annex.md`

## 規範性の考え方
この annex は `01_core/` を上書きしません。  
ただし、`foundational_role: recommended_foundational_extension` の項目は、研究発展・高説明責任実装・将来の v2 準備として採用を推奨します。

## どういうときに読むか
- 自然言語入力の誤正規化が多い
- H2 が粗すぎて説明責任に足りない
- 単一スコア化が危険
- approval の失効や hold の期限を実装したい
- rollback を由来単位で説明したい

## どこから先は institutional annex か
次の論点が前景化したら、`../08_institutional_annex/` へ進みます。

- source quality では足りず、証言・専門性・defeater を扱いたい
- 複数レビューを合議として整合的に残したい
- decision outcome を gate / baseline / artifact に結び付けたい
- 現場の人の停止権・引継ぎ・訓練完了を状態として管理したい

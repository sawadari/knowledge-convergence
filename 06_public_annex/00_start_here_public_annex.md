# 公開 annex の入口

`06_public_annex/` は、`01_core/` の公開仕様だけでは粗くなりやすい補助論点を、**raw supplement より薄く・公開配布面として読みやすく** 再編集した層です。

## 位置づけ
- **最優先の正本**: `01_core/`
- **その次の補助正本**: `06_public_annex/`
- **基礎発展 annex**: `../07_foundational_annex/`
- **制度運用発展 annex**: `../08_institutional_annex/`
- **さらに元の研究補助束**: `02_supplements/`

つまり、公開向けには **core → annex → foundational annex → institutional annex → raw supplement** の順で読む想定です。

## annex に入れたもの
- 権限・承認・責任境界
- SLA / confidence / semantic delta の補助較正
- 監査ログ、匿名化、保持、bounded summary
- Hold reason の関係語彙と positive state
- route family の core / extension 境界
- externality budget の baseline 較正

## annex に入れなかったもの
- scheduler / federation の大型拡張
- bridge token / witness packet / serialization の重い細部
- multi-session quota / debt / reservation の内部運用
- 長い migration / reverse / replay chain の細密機構
- 組織固有の数表や vendor 寄り packet 形

## どこから先は foundational annex / institutional annex か
次の論点は `06_public_annex/` ではなく発展 annex 側にあります。

### foundational
- speech act / evidentiality / presupposition
- ambiguity の細分化
- argument graph と four-valued support status
- outranking / measurement profile
- provenance trace / temporal guard

### institutional
- testimony / expertise scope / defeater
- premise-based / conclusion-based aggregation
- minority report / consistency repair
- baseline / gate / transition package / ops feedback
- human role / override right / training readiness / manual fallback

## 最初に読む順番
1. `public_annex_crosswalk_v1.yaml`
2. `public_annex_concepts_v1.yaml`
3. `public_annex_formalization_v1.yaml`
4. 必要なら `publication_filter_report_v1.yaml`
5. 具体例を見るなら `examples/`
6. 発話解釈や競合意味論を足すなら `../07_foundational_annex/00_start_here_foundational_annex.md`
7. 合議や運用保証を足すなら `../08_institutional_annex/00_start_here_institutional_annex.md`

## 規範性の考え方
annex は `01_core/` を上書きしません。  
ただし `public_spec_role: recommended_extension` の項目は、公開実装や外部レビューで **追加採用してよい標準候補** として扱えるようにしています。

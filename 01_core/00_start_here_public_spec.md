# 公開仕様の入口

この `01_core/` には、役割の違う文書が共存しています。

## このフォルダの八層構造
### 1. 公開仕様レイヤ
外部説明・レビュー・実装着手のために、語彙と最低契約を安定化した文書群です。

- `concepts_public_spec_v1.yaml`
- `formalization_public_spec_v1.yaml`
- `canonical_public_data_contract_v1.yaml`
- `conformance_profiles_public_v1.yaml`
- `implementation_quickstart_public_v1.md`
- `public_term_glossary_v1.md`
- `json_schema/`
- `examples/`

### 2. 公開 annex レイヤ
公開仕様を厚くする補助規則を、raw supplement より短く再編集した層です。

- `../06_public_annex/00_start_here_public_annex.md`
- `../06_public_annex/public_annex_concepts_v1.yaml`
- `../06_public_annex/public_annex_formalization_v1.yaml`
- `../06_public_annex/public_annex_crosswalk_v1.yaml`

### 3. 基礎発展レイヤ
知識収束学を言語学・数学・実装検証の方向へ伸ばすための追加採用レイヤです。  
core を上書きせず、上流の発話解釈と下流の競合・多基準・由来・時相を増設します。

- `foundational_extension_profiles_v1.yaml`
- `foundational_contract_addendum_v1.yaml`
- `foundational_glossary_addendum_v1.md`
- `../07_foundational_annex/00_start_here_foundational_annex.md`
- `../07_foundational_annex/foundational_language_annex_v1.yaml`
- `../07_foundational_annex/foundational_mathematical_annex_v1.yaml`
- `../07_foundational_annex/foundational_crosswalk_v1.yaml`

### 4. 制度運用発展レイヤ
知識状態を、正当化された証言・合議・ライフサイクル成果物・人間中心運用へ接続する追加採用レイヤです。  
core と foundational を上書きせず、制度・運用・現場保証を増設します。

- `institutional_extension_profiles_v1.yaml`
- `institutional_contract_addendum_v1.yaml`
- `institutional_glossary_addendum_v1.md`
- `../08_institutional_annex/00_start_here_institutional_annex.md`
- `../08_institutional_annex/institutional_crosswalk_v1.yaml`
- `../08_institutional_annex/epistemic_justification_annex_v1.yaml`
- `../08_institutional_annex/collective_judgment_annex_v1.yaml`
- `../08_institutional_annex/systems_lifecycle_annex_v1.yaml`
- `../08_institutional_annex/human_centered_operations_annex_v1.yaml`

### 5. 制度運用適合検査レイヤ
制度運用発展 annex を、実際に pass / warn / fail で検査するためのレイヤです。  
schema 検査だけでなく、quorum、training readiness、baseline、qualified testimony などの**意味規則**を扱います。

- `../09_conformance_suite/00_start_here_conformance_suite.md`
- `../09_conformance_suite/institutional_validation_rulebook_v1.yaml`
- `../09_conformance_suite/institutional_conformance_matrix_v1.yaml`
- `../09_conformance_suite/institutional_conformance_test_suite_v1.yaml`
- `../09_conformance_suite/validation_report_v1.yaml`

### 6. SEシステム応用統合レイヤ
知識収束学を、システム開発・組織構造・人間系・AIエージェント運用へ接続する応用 annex です。
v1.1 では、この応用統合で露出した弱点のうち、ドメイン妥当性収束、AI実行主体、意味ある人間監督、組織トポロジー、収束計量を core 側へ昇格しました。

- `../10_se_system_annex/00_start_here_se_system_annex.md`
- `../10_se_system_annex/se_system_theory_integration_v1.md`
- `../10_se_system_annex/se_system_theory_review_and_corrections_v1.md`
- `../10_se_system_annex/se_system_extension_profiles_v1.yaml`
- `../10_se_system_annex/se_system_reference_architecture_v1.yaml`
- `../10_se_system_annex/se_system_lint_rulebook_v1.yaml`

### 7. core revision annex レイヤ
SEシステム統合後のレビューを受けた v1.1 core 改訂内容です。

- `../11_core_revision_annex/00_start_here_core_revision_annex.md`
- `../11_core_revision_annex/core_theory_revision_report_v1_1.md`
- `../11_core_revision_annex/migration_guide_v1_to_v1_1.md`
- `../11_core_revision_annex/conformance_delta_v1_1.yaml`

### 8. 理論コアレイヤ
研究由来の概念本文と形式本文です。

- `concepts_core_v1.yaml`
- `formalization_core_v1.yaml`
- `knowledge_convergence_report_for_beginners_repackaged_v1.md`

## 読み分け
- 「何を主張している理論か」を知りたいなら `concepts_public_spec_v1.yaml`
- 「何を最低限実装すればよいか」を知りたいなら `canonical_public_data_contract_v1.yaml`
- 「既存の準拠段階」を知りたいなら `conformance_profiles_public_v1.yaml`
- 「言語・数学の発展採用段階」を知りたいなら `foundational_extension_profiles_v1.yaml`
- 「正当化・合議・運用保証の発展採用段階」を知りたいなら `institutional_extension_profiles_v1.yaml`
- 「実データ形を見たい」なら `examples/` と `json_schema/`
- 「制度運用 annex をどう検査するか」を知りたいなら `../09_conformance_suite/00_start_here_conformance_suite.md`
- 「SEシステム、組織構造、人間系、AIエージェント運用への統合」を知りたいなら `../10_se_system_annex/00_start_here_se_system_annex.md`
- 「v1.1でcoreの何を修正したか」を知りたいなら `../11_core_revision_annex/00_start_here_core_revision_annex.md`
- 「より厳密な背景」を見たいなら `*_core_v1.yaml`

## この版で固定した公開上の約束
1. 生成物は、そのままでは知識ではない
2. 収束は唯一解の強制を意味しない
3. 認識収束、統治収束、ドメイン妥当性収束は分けて扱う
4. Hold は失敗ではなく正規の状態である
5. AI は候補生成や補助主体だけでなく限定された実行主体にもなれるが、既定の結果責任主体にはしない
6. human-in-the-loop は安全性を自動保証しない
7. 組織構造と人間系は外部背景ではなくKへ接続される一級要素である

## この版で追加採用できるもの
### 基礎発展
- 発話解釈 envelope
- speech act / evidentiality / presupposition / deictic anchor
- 曖昧性の細分化と gradable term の threshold profile
- 4値の support status と argument graph
- outranking / measurement profile / interval uncertainty
- provenance trace / temporal guard / validity interval

### 制度運用発展
- 証言・専門性・defeater を扱う epistemic justification packet
- premise-based / conclusion-based を明示する aggregation rule profile
- minority report / consistency repair / dissent trace
- baseline / gate / artifact / transition package / ops feedback
- human roles / override rights / explanation scope / training readiness / manual fallback


### SEシステム応用統合
- SEシステムを開発意思決定OSとして扱う理論統合
- `K_SE=(G_SE,C_SE,E_SE,V_SE,R_SE,H_SE)` の対応
- 認識収束・統治収束に加えた工学的妥当性収束
- 組織・人間系を一級要素として扱う role / authority / training / fallback
- AIエージェント委任の authority envelope / audit log / rollback path
- SysMLに依存しない自然言語・準形式・DSL・形式言語の表現階段

## この版で公開仕様の core にまだ含めないもの
- scheduler / federation 系の大型拡張
- 研究ログ
- 未整理の open point 詳細
- ドメイン固有の細密キャリブレーション

それらは引き続き `02_supplements/` 以降に残しています。  
言語学・数学方向の発展は `foundational_extension_profiles_v1.yaml` と `../07_foundational_annex/`、  
制度運用方向の発展は `institutional_extension_profiles_v1.yaml` と `../08_institutional_annex/` を見てください。
制度運用 packet の適合検査は `../09_conformance_suite/` を見てください。
SEシステムへの応用統合は `../10_se_system_annex/` を見てください。
v1.1 core改訂の理由と移行方法は `../11_core_revision_annex/` を見てください。

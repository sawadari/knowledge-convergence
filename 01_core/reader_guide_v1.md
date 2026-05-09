# Reader Guide

## まず何を見るか
### 外部説明・レビュー
1. `00_start_here_public_spec.md`
2. `concepts_public_spec_v1.yaml`
3. `formalization_public_spec_v1.yaml`

### 実装
1. `implementation_quickstart_public_v1.md`
2. `canonical_public_data_contract_v1.yaml`
3. `conformance_profiles_public_v1.yaml`
4. `json_schema/`
5. `examples/`

### 公開補助 annex
1. `../06_public_annex/00_start_here_public_annex.md`
2. `../06_public_annex/public_annex_crosswalk_v1.yaml`
3. `../06_public_annex/public_annex_concepts_v1.yaml`
4. `../06_public_annex/public_annex_formalization_v1.yaml`

### 基礎発展 annex
1. `foundational_extension_profiles_v1.yaml`
2. `foundational_contract_addendum_v1.yaml`
3. `../07_foundational_annex/00_start_here_foundational_annex.md`
4. `../07_foundational_annex/foundational_crosswalk_v1.yaml`
5. `../07_foundational_annex/foundational_language_annex_v1.yaml`
6. `../07_foundational_annex/foundational_mathematical_annex_v1.yaml`

### 制度運用発展 annex
1. `institutional_extension_profiles_v1.yaml`
2. `institutional_contract_addendum_v1.yaml`
3. `../08_institutional_annex/00_start_here_institutional_annex.md`
4. `../08_institutional_annex/institutional_crosswalk_v1.yaml`
5. `../08_institutional_annex/epistemic_justification_annex_v1.yaml`
6. `../08_institutional_annex/collective_judgment_annex_v1.yaml`
7. `../08_institutional_annex/systems_lifecycle_annex_v1.yaml`
8. `../08_institutional_annex/human_centered_operations_annex_v1.yaml`

## 読み方のコツ
- core だけで十分な導入なら `01_core/` から出なくてよい
- governance 細部が必要なときだけ `06_public_annex/` を足す
- 自然言語入力・競合意味論・多基準判断・時間拘束が重くなったら `07_foundational_annex/` を足す
- 証言の正当化・合議・運用ゲート・人間中心監督が重くなったら `08_institutional_annex/` を足す
- raw research を辿るのは最後でよい


---

## v1.1 追記: 三層収束として読む

v1 では、認識収束と統治収束の二層を中心に読む。v1.1 では、これに `domain_validity_convergence` を加える。

```text
認識収束: 内容として説明できるか
統治収束: 誰がどの条件で実行・保留・差戻しできるか
ドメイン妥当性収束: 対象ドメインで実際に使ってよいか
```

SEシステムでは、第三層は工学的妥当性収束として、要求・設計・Verification・Validation・運用フィードバックへ接続される。

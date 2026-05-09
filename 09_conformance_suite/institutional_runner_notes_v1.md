# 制度運用適合 runner の使い方

## 目的
`09_conformance_suite/tools/run_institutional_conformance.py` は、

1. `08_institutional_annex/json_schema/` の packet schema を使った構造検査
2. `institutional_validation_rulebook_v1.yaml` に対応する semantic rule 検査
3. `institutional_conformance_test_suite_v1.yaml` の期待結果照合

を一度に行うための参照実装です。

## 依存
- Python 3.10+
- `PyYAML`
- `jsonschema`

## 実行
パッケージ root で次を実行します。

```bash
python 09_conformance_suite/tools/run_institutional_conformance.py
```

出力先を変えたいときは:

```bash
python 09_conformance_suite/tools/run_institutional_conformance.py --output my_report.yaml
```

## 判定
- `pass`: error と warning が無い
- `warn`: warning はあるが error は無い
- `fail`: error がある

## 位置づけ
この runner は **参照用** です。  
実運用では rule id を CI、review gate、release gate、監査チェックへ写像して使う想定です。

## report の overall_result
`overall_result` は **suite-level の期待一致** を表します。負例が fail していても、それが期待通りなら suite 全体は `pass` です。

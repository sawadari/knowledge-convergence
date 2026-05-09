# 制度運用適合検査 suite の入口

`09_conformance_suite/` は、`08_institutional_annex/` で追加した packet 群を **実際に検査する層** です。

## ここにあるもの
- `institutional_validation_rulebook_v1.yaml`
  - rule id 単位の semantic validation 規則
- `institutional_conformance_matrix_v1.yaml`
  - 各 profile と schema / rule / test の対応表
- `institutional_conformance_test_suite_v1.yaml`
  - pass / warn / fail を返す試験ケース一覧
- `validation_report_v1.yaml`
  - 現在の参照レポート
- `json_schema/`
  - conformance finding / report の schema
- `test_vectors/`
  - 既存 example を補う負例・警告例・例外許容例
- `tools/run_institutional_conformance.py`
  - 参照 runner

## 読み順
1. `institutional_conformance_matrix_v1.yaml`
2. `institutional_validation_rulebook_v1.yaml`
3. `institutional_conformance_test_suite_v1.yaml`
4. `validation_report_v1.yaml`
5. `tools/run_institutional_conformance.py`

## この suite が狙うこと
- schema を通るだけでは見逃す institutional failure を拾う
- rule id 単位で CI / review gate / release gate に結び付ける
- institutional annex を「語彙」から「検査可能な運用仕様」へ進める

## 代表的に拾うもの
- expert label だけで high-risk execute していないか
- contested conclusion に minority report と repair があるか
- baseline / validation / ops feedback が execute と接続しているか
- training incomplete や no fallback を安全に止められるか

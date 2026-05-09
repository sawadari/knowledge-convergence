# 公開仕様化メモ

この版は、前段の「再パッケージ版」をさらに外部配布向けへ整えた第2段階です。

## 追加したもの
- 公開概念仕様
- 公開形式仕様
- 公開データ契約
- 準拠プロファイル
- 用語集
- 実装クイックスタート
- JSON Schema
- 具体例

## 変えていないもの
- 研究ログ
- 大型拡張パック
- 元フラット構成
- 凍結済み v1 の理論上の立場

## 目的
理論を薄めることではなく、次の3者が同じ入口に立てるようにすることです。

- 外部読者
- 実装者
- レビュー担当

## 読み方
- 説明用: `concepts_public_spec_v1.yaml`
- 形式用: `formalization_public_spec_v1.yaml`
- 実装用: `canonical_public_data_contract_v1.yaml`
- 試験用: `conformance_profiles_public_v1.yaml`


---

## v1.1 core revision, 2026-05-08

この版では、SEシステム統合後の理論レビューに基づき、core を次のように修正した。

- 二層収束を後方互換として残しつつ、`domain_validity_convergence` を第三層として追加した。
- `agent_execution_governance` を追加し、AI/agent を限定された実行主体として扱えるようにした。
- `meaningful_human_oversight` を追加し、形式的な human-in-the-loop を不十分と明示した。
- `organization_topology` を追加し、組織構造・人間系を一級要素にした。
- `convergence_measurement` を追加し、単一スコアで blocker を相殺しない方針を明示した。
- JSON Schema と public data contract に、domain validity / agent execution / human oversight / organization / metrics の packet を追加した。

互換性: `K=(G,C,E,V,R,H)`、既存 branch 語彙、KC-E1/KC-G1/KC-D1/KC-A1 は維持する。

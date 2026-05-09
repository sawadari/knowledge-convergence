# core revision annex v1.1 の入口

この annex は、SEシステム統合後のレビューを受けて、知識収束学の core をどのように改善したかを説明する。

## 主な変更

- 二層収束を三層収束へ拡張した。
- 第三層を汎用的には `domain_validity_convergence` と呼び、SEシステムでは `engineering_validity_convergence` と呼ぶ。
- AI/agent を限定された実行主体として扱うため、`agent_execution_envelope` を追加した。
- 人間の形式的承認ではなく、意味ある人間監督を要求した。
- 組織構造・人間系を SEシステム内の一級要素として扱った。
- 収束状態を単一スコアではなく、多次元・blocker-preserving に計量する方針を追加した。

## 読む順序

1. `core_theory_revision_report_v1_1.md`
2. `migration_guide_v1_to_v1_1.md`
3. `conformance_delta_v1_1.yaml`
4. `examples/`

# 知識収束学 v1.1 公開仕様＋SEシステム core 改訂版

このZIPは、前版の SEシステム統合版を土台にし、core そのものを改善した v1.1 版です。

## v1.1でcoreへ昇格したこと

- `domain_validity_convergence`: 認識・統治に加えて、対象ドメインで本当に使ってよいかを判定する第三層
- `agent_execution_governance`: AI/agent を限定された実行主体として扱うための権限・監査・停止・rollback
- `meaningful_human_oversight`: 形式的 human-in-the-loop ではなく、実効的な人間介入可能性
- `organization_topology`: 組織構造・人間系・専門性・意思決定権・レビュー能力
- `convergence_measurement`: 単一スコアではなく、多次元かつ blocker-preserving な収束計量

詳細は `11_core_revision_annex/` を参照してください。

---

## 前版から引き継いだ構成

このZIPは、前版で整備した `institutional_annex`、`09_conformance_suite`、`10_se_system_annex` を引き継ぎ、そのうえで core を v1.1 として補強した版です。

## この版で追加したこと
- `09_conformance_suite/` を新設
- 制度運用 annex 用の **検査ルール集** を追加
- `KC-T1 / KC-S1 / KC-O1 / KC-H1` ごとの **適合マトリクス** を追加
- pass / warn / fail を返せる **テストスイート** を追加
- 既存 institutional 例と負例ベクトルをまとめて検査した **validation report** を追加
- 実装依存に寄せすぎない **Python runner** を追加
- `10_se_system_annex/` を新設
- 知識収束学を **システム開発・組織構造・人間系・AIエージェント運用** へ接続する理論統合を追加
- SEシステム用の `KC-SE0`〜`KC-SE5` プロファイル、参照アーキテクチャ、SE Lint ルール集、例を追加

## この版の改善方針
このv1.1版は、`K = (G, C, E, V, R, H)` の表記と既存 branch 語彙を維持しつつ、core に第三層 `domain_validity_convergence` と、AI実行主体・人間監督・組織トポロジー・収束計量の補助packetを追加します。
そのうえで、

- どの packet を持てば `KC-T1 / KC-S1 / KC-O1 / KC-H1` に適合したと言えるか
- JSON Schema だけでは拾えない **意味規則** をどう検査するか
- 既存 example がどこまで pass し、どのような負例が fail するか
- 実装チームが rule id 単位で CI / review gate に接続できるか

を、**追加の conformance suite** として整備しています。

## この版の立場
- `01_core/` は canonical public contract
- `06_public_annex/` は公開配布向けの補助 annex
- `07_foundational_annex/` は言語学・数学・由来・時相の基礎拡張 annex
- `08_institutional_annex/` は認識論・合議設計・運用工学・HCI を扱う制度運用発展 annex
- `09_conformance_suite/` は制度運用発展 packet を検査するための適合スイート
- `10_se_system_annex/` は知識収束学をSEシステム、組織構造、人間系、AIエージェント運用へ接続する応用統合 annex
- `02_supplements/` は raw research supplement の source pool
- `03_extensions/`、`04_operations/`、`05_logs/`、`99_archive/` は研究運用と厚みを保持

## 最初の入口
- 外部読者・レビュー担当: `01_core/00_start_here_public_spec.md`
- 実装者: `01_core/implementation_quickstart_public_v1.md`
- 制度運用発展の語彙を見る人: `08_institutional_annex/00_start_here_institutional_annex.md`
- 実際に制度運用 packet を検査したい人: `09_conformance_suite/00_start_here_conformance_suite.md`
- SEシステム統合を読みたい人: `10_se_system_annex/00_start_here_se_system_annex.md`
- 追加採用プロファイルを見る人: `01_core/institutional_extension_profiles_v1.yaml`

## 意味変更ポリシー
このv1.1版は、理論の芯である `K=(G,C,E,V,R,H)` と branch 語彙を維持しながら、二層収束を三層収束へ拡張します。
**制度運用 annex を保存したまま、SEシステム統合で露出した弱点を core 側に反映し、検査可能な規則・試験ケース・実行例を足した版** です。

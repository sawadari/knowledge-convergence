# SEシステム統合 annex の入口

`10_se_system_annex/` は、知識収束学を **システム開発・組織構造・人間系・AIエージェント運用** へ接続するための応用統合 annex です。

この annex は、`K=(G,C,E,V,R,H)` をシステム開発の「コードを書く前に決める仕事」「複数専門家の合意形成」「実装・業務自動化エージェントへの委任」に適用するための拡張です。v1.1 では、この annex で露出した弱点のうち、ドメイン妥当性収束、AI実行主体、意味ある人間監督、組織トポロジー、収束計量を `01_core/` 側にも昇格しました。

## この annex が足すもの

### 1. SEシステムの理論統合
- SEシステムを「AIコーディング支援」ではなく、**開発意思決定OS** として定義する。
- システム開発における `K_SE=(G_SE,C_SE,E_SE,V_SE,R_SE,H_SE)` の対応を示す。
- 認識収束・統治収束に加えて、**工学的妥当性収束** を扱う。

### 2. 組織構造・人間系の一級要素化
- 組織、役割、意思決定権限、専門性、訓練状態、停止権、エスカレーション経路を、外部条件ではなくシステム要素として扱う。
- 人間は単なる承認者ではなく、目的設定者、判断者、責任主体、例外処理者として扱う。

### 3. AIエージェント時代への補強
- AIを「候補生成者」だけではなく、限定された **実行主体** として扱う。
- ただし、AIに既定の結果責任を持たせない。
- agent identity、authority envelope、sandbox、audit log、rollback path、human review gate を必須化する。

### 4. 表現言語の非依存化
- SysMLを前提にしない。
- 自然言語、構造化自然言語、準形式言語、DSL、形式言語、実行可能モデルを「形式化の階段」として扱う。
- 正本は特定図法ではなく、意味中間表現と根拠付き関係である。

## 主要ファイル

- `se_system_theory_integration_v1.md`  
  SEシステムと知識収束学の統合理論本文。

- `se_system_theory_review_and_corrections_v1.md`  
  現在のAI開発状況を踏まえた、理論基盤の弱点・補強点・変更しない点のレビュー。

- `se_system_crosswalk_v1.yaml`  
  SEシステム概念と `K=(G,C,E,V,R,H)`、institutional profiles、実装コンポーネントの対応表。

- `se_system_extension_profiles_v1.yaml`  
  SEシステムを段階採用するための `KC-SE0`〜`KC-SE5` プロファイル。

- `se_system_reference_architecture_v1.yaml`  
  SEシステムの参照アーキテクチャ。Convergence plane、Execution plane、Governance plane を分ける。

- `se_system_lint_rulebook_v1.yaml`  
  SEシステム用の意味検査ルール。コード実装前のDecision、V&V、組織、人間、AI委任、表現形式を検査する。

- `examples/`  
  SEシステムで扱う典型ケース。

- `json_schema/`  
  最小 packet の参考 schema。

## 読む順番

1. `../01_core/00_start_here_public_spec.md`
2. `../07_foundational_annex/00_start_here_foundational_annex.md`
3. `../08_institutional_annex/00_start_here_institutional_annex.md`
4. `se_system_theory_integration_v1.md`
5. `se_system_theory_review_and_corrections_v1.md`
6. `se_system_extension_profiles_v1.yaml`
7. `se_system_lint_rulebook_v1.yaml`

## この annex の立場

SEシステムは、AIコーディング、OpenClaw型業務実行エージェント、従来の要求管理ツール、SysMLツールのいずれかと競合するものではありません。

この annex では、関係を次のように置きます。

```text
SEシステム
  = 何を、なぜ、どの制約で、誰の責任で、どう検証するかを収束させる基盤

AIコーディングエージェント
  = 承認済みの仕様・制約・設計判断をもとにコード、テスト、PRを生成する実行者

OpenClaw型業務エージェント
  = 既存アプリ、ブラウザ、Slack、Discord、カレンダー、チケットなどを操作する実行者
```

したがって、SEシステムの主目的は「実行速度」ではありません。主目的は、**実行してよい対象を根拠付きで定義し、変更に耐える知識状態として管理すること**です。

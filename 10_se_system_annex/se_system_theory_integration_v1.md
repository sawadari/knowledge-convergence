# 知識収束学とSEシステムの統合理論 v1

作成日: 2026-05-08  
位置づけ: `10_se_system_annex` の主文書  
前提: `01_core/` の canonical public contract を上書きしない

---

## 1. 統合命題

この文書では、SEシステムを次のように定義する。

> **SEシステムとは、コードを書く前に必要となる事業・運用・要求・制約・設計判断・検証方針・専門家合意・組織責任を、根拠付きで、追跡可能で、検証可能で、変更可能な知識状態へ収束させ、AIエージェント群と人間が共同で扱うための開発意思決定OSである。**

この定義では、SEシステムは単なるMBSEツールではない。SEシステムは、要求管理ツール、SysMLエディタ、AIコーディングツール、業務自動化エージェントの上位概念でもない。SEシステムは、それらを接続し、**何を実行してよいかを決めるための知識収束基盤**である。

知識収束学は、生成物や発言をそのまま知識とみなさない。知識収束学は、主張、文脈、根拠、価値基準、責任、履歴を束ね、実行・保留・差戻しを判断できる状態を知識とみなす。SEシステムは、この考え方をシステム開発に適用したものである。

---

## 2. なぜSEシステムが必要か

### 2.1 コードを書く前に決めることがある

システム開発では、コードを書く前に次を決める必要がある。

- 誰のためのシステムか
- どの事業価値を実現するか
- どの業務・運用を変えるか
- システム境界をどこに置くか
- 人間、ソフトウェア、ハードウェア、業務プロセスをどう分担するか
- どの制約を受けるか
- どのリスクを許容するか
- どの性能、安全性、保守性、拡張性を満たすか
- 何をもって成功と判断するか
- どの方法で検証し、どの方法で妥当性確認するか

これらはコードを書くことによって自然には解決しない。コードは、すでに決めた方針や仕様を実装することには強い。しかし、コードは「そもそも何を作るべきか」「その要求は事業価値に結びつくか」「どの専門家の制約を優先するか」「その成功条件は妥当か」を自動的には決めない。

### 2.2 コード以前の作業量は大きい

大規模・高リスク・複数専門領域のシステムでは、コード以前の作業量が大きい。事業構想、業務設計、利用者観察、ステークホルダ調整、要求抽出、制約整理、アーキテクチャ判断、V&V方針、変更影響分析、レビュー、承認が存在する。

AIコーディングが実装速度を上げるほど、上流の定義品質の不足はより危険になる。間違った対象を高速に実装できるからである。

### 2.3 システム開発はソフトウェア開発より広い

システム開発は、ソフトウェアだけで閉じない。対象には、ハードウェア、メカ、電気電子、制御、安全、品質、製造、保守、運用、法規、サプライチェーン、業務プロセス、人間の作業、組織の責任分担が含まれる。

したがって、SEシステムは、AIコーディングツールよりも広いスコープを持つ。SEシステムは、ソフトウェア実装の生産性ではなく、**システムとして成立するための意思決定品質**を扱う。

### 2.4 複数専門家の合意形成が本質である

システム開発では、複数の専門家が同じ対象を異なる評価軸で見る。ソフトウェア担当者は実装容易性を重視し、品質保証担当者は検証可能性を重視し、安全担当者は危害低減を重視し、事業責任者は市場価値と投資対効果を重視する。

SEシステムは、この専門家間の判断を単なる会議録として保存するのではなく、Decision、Rationale、Dissent、Evidence、Assumption、Reopen condition として扱う。

### 2.5 システムズエンジニアリングを使う理由

システムズエンジニアリングを使う理由は、SEが「世界的に失敗を体系化してきた知識」だからである。顧客ニーズの誤解、要求の曖昧性、要求と検証の断絶、専門家間の制約衝突、設計判断根拠の消失、変更影響漏れ、Verificationは通ったがValidationで失敗する問題は、繰り返し発生してきた。

SEシステムは、この失敗回避の知識を、AI時代のソフトウェア基盤として再実装する。

---

## 3. 知識収束学から見たSEシステム

知識収束学の正本表現は、次である。

```text
K = (G, C, E, V, R, H)
```

SEシステムでは、これを次のように具体化する。

```text
K_SE = (G_SE, C_SE, E_SE, V_SE, R_SE, H_SE)
```

### 3.1 G_SE: 意味構造

`G_SE` は、システム開発上の意味関係を保持する。

- Opportunity / Mission / Business Goal
- Stakeholder / Need / Pain point
- Operational Scenario / Use Case / Context
- System Boundary / External Actor / Enabling System
- Requirement / Constraint / Assumption
- Function / Behavior / State / Mode
- Component / Role / Process / Interface
- Option / Decision / Trade-off
- Verification / Validation / Test / Simulation
- Risk / Hazard / Mitigation
- Implementation Task / Code Artifact / Workflow Automation Task

重要なのは、これらを要素として保存することではなく、関係として保存することである。

```text
Need derives Requirement
Requirement constrains Function
Function allocatedTo Component / Role / Process
Decision selects Option
Decision rejects Option
Decision justifiedBy Evidence
Requirement verifiedBy Verification
Need validatedBy Operational Scenario
Change impacts Requirement / Interface / Test / Role / Process
```

### 3.2 C_SE: 文脈・境界・前提

`C_SE` は、判断の適用条件を保持する。

- ライフサイクル段階
- システム境界
- 対象市場・対象顧客・対象運用環境
- 想定ユースケース
- 法規・規格・契約上の制約
- 事業上の制約
- 技術前提
- 組織前提
- 時点、有効期間、freshness window

SEでは、同じ要求文でも文脈が変われば意味が変わる。したがって、文脈を要求から切り離して扱ってはいけない。

### 3.3 E_SE: 根拠

`E_SE` は、判断に使う根拠を保持する。

- 顧客ヒアリング
- 議事録
- 市場データ
- 実験・試験結果
- シミュレーション結果
- 過去不具合
- 法規・規格
- 専門家証言
- コード・ログ・テレメトリ
- 運用フィードバック

AIが生成した文章は、根拠ではなく候補である。AI出力を根拠として使う場合でも、どの入力、どのツール、どのモデル、どの検査を経たかを明示しなければならない。

### 3.4 V_SE: 価値基準・判定基準

`V_SE` は、採択や棄却の基準を保持する。

- 事業価値
- 顧客価値
- 安全性
- 品質
- コスト
- 納期
- 保守性
- 製造容易性
- 法規適合
- リスク許容度
- Validation基準
- Trade-off基準

SEシステムでは、単なる正誤判定だけでは不十分である。実際のシステム開発では、複数の価値基準が衝突する。SEシステムは、価値衝突を隠さず、どの基準をどの重み・根拠・責任で優先したかを残す必要がある。

### 3.5 R_SE: 責任・権限・委任

`R_SE` は、人間、組織、AIエージェントの責任・権限・委任を保持する。

- Decision owner
- Responsible role
- Accountable role
- Reviewer
- Domain expert
- Safety lead
- Quality lead
- Operator
- Auditor
- AI agent identity
- Delegation policy
- Authority envelope
- Stop / override right
- Escalation path

AIエージェントを実行主体に含めることはできる。しかし、AIエージェントを既定の結果責任主体にはしない。結果責任は、人間または制度上の役割に束縛する。

### 3.6 H_SE: 履歴・差戻し・再開

`H_SE` は、判断と変更の履歴を保持する。

- Baseline
- Revision
- Decision history
- Dissent trace
- Review comment
- Approval log
- Agent action log
- Test result history
- Incident report
- Reopen event
- Rollback event

SEシステムでは、変更時に「何が変わったか」だけでなく、「どの前提が崩れたか」「どの判断を再検討すべきか」を追える必要がある。

---

## 4. 認識収束・統治収束・工学的妥当性収束

既存の知識収束学は、認識収束と統治収束を分ける。この分離は正しい。ただし、SEシステムでは第三の観点を明示する必要がある。

```text
認識収束: 内容として説明可能か
統治収束: 誰がどの条件で実行・保留・差戻しできるか
工学的妥当性収束: システムとして目的・運用・検証・妥当性確認に耐えるか
```

認識収束と統治収束が成立していても、システムとして妥当とは限らない。たとえば、要求が根拠付きで承認されていても、Validationシナリオが存在しないなら、顧客価値に合うかは未確定である。

したがって、SEシステムでは次の原則を追加する。

> **SE収束は、知識状態が説明可能かつ統治可能であることに加えて、Verification / Validation / 運用フィードバックへ接続されている必要がある。**

これは既存coreの上書きではない。SEドメインにおける追加採用条件である。

---

## 5. SEシステムの三つの平面

SEシステムは、次の三平面に分けて設計する。

```text
[1] Convergence Plane
    何を、なぜ、どの制約で、どう検証するかを収束させる

[2] Execution Plane
    承認された内容をコード、テスト、資料、業務操作、通知、チケットに変換する

[3] Governance Plane
    人間・組織・AIエージェントの責任、権限、監査、停止、再開を管理する
```

AIコーディングやOpenClaw型エージェントは、主に Execution Plane に属する。SEシステムは、主に Convergence Plane と Governance Plane を担う。

---

## 6. 参照アーキテクチャ

SEシステムの最小アーキテクチャは、次である。

```text
[7] Human / Organization Workbench
[6] Agent Delegation & Orchestration
[5] SE Lint / Reasoning / Simulation
[4] Decision Ledger / Trade-off Ledger
[3] Canonical SE Graph
[2] Evidence & Context Store
[1] Integration Layer
```

### 6.1 Integration Layer

既存の資料・ツール・リポジトリ・運用系を接続する。

- 企画書
- 顧客ヒアリング
- 議事録
- Excel要求表
- PowerPoint設計資料
- 法規・規格
- FMEA / FTA
- PLM / ALM
- Git / Issue / PR
- テスト結果
- シミュレーション結果
- 運用ログ

SEシステムは、最初から既存ツールを置き換えるべきではない。まずは意味的接続を作るべきである。

### 6.2 Evidence & Context Store

原文、根拠、時点、文脈を保存する。AI要約を正本にしない。AI要約は Evidence を参照する候補として扱う。

### 6.3 Canonical SE Graph

正本は、図や表ではなく、型付きの意味グラフである。SysML、UML、BPMN、要求表、DSL、形式仕様はビューまたは投影である。

### 6.4 Decision Ledger / Trade-off Ledger

コードを書く前にある「決める仕事」を正本化する。

```text
Issue: 何が未決か
Option: どの選択肢があるか
Criteria: 何で比較するか
Decision: 何を選んだか
Rationale: なぜ選んだか
Rejected option: 何を捨てたか
Assumption: どの前提に依存するか
Reopen condition: どの条件で再検討するか
```

### 6.5 SE Lint / Reasoning / Simulation

AI時代のSEシステムでは、SE用の判定器が必要である。コード開発ではコンパイラ、型チェック、lint、テスト、CIが判定器である。SEシステムでは次が判定器になる。

- 根拠なし要求の検出
- 検証不能要求の検出
- Validation未接続の検出
- 制約と設計方針の混同検出
- 重要Decisionの根拠不足検出
- 却下案の不在検出
- 変更影響未評価の検出
- 専門家レビュー未実施の検出
- AIエージェント委任権限の欠落検出
- 人間の停止権・手動代替の欠落検出

### 6.6 Agent Delegation & Orchestration

AIエージェントは、SEシステムの正本を直接書き換えない。AIエージェントは、差分候補、実行結果、ログ、失敗理由を返す。

AIエージェントには次を必須とする。

- agent_id
- capability_scope
- authority_envelope
- sandbox / permission
- input_knowledge_refs
- output_artifact_refs
- audit_log_refs
- human_review_gate
- rollback_path

### 6.7 Human / Organization Workbench

人間は、単なる承認者ではない。人間は、目的設定者、判断者、専門家、責任主体、例外処理者である。SEシステムのUIは、チャットだけでは不足する。次のワークベンチが必要である。

- Mission / Business Goal Workspace
- Stakeholder / Scenario Workspace
- Decision Board
- Trade-off Workspace
- Requirement / V&V Workspace
- Change Impact View
- Agent Task Board
- Human Oversight View
- Organization Responsibility View

---

## 7. 組織構造と人間系をSEシステム内に含める

SEシステムでは、組織構造と人間系を外部環境として扱わない。組織構造と人間系は、システム開発を成立させる要素である。

### 7.1 組織をシステム要素として扱う

SEシステムは、次を保持する。

- 役割
- 権限
- 専門性範囲
- 意思決定権
- 承認条件
- 代替者
- 利害関係
- 責任分離
- エスカレーション経路
- 訓練状態
- 認知負荷
- 受容状態

これは、単なる組織図ではない。SEシステムに必要なのは、**どの判断を誰がどの根拠で担えるか**である。

### 7.2 標準役割

SEシステムでは、少なくとも次の役割を置く。

| 役割 | 主責務 |
|---|---|
| Mission / Business Owner | 事業目的、顧客価値、投資判断を持つ |
| Chief Systems Engineer | システム境界、要求、設計判断、V&V方針を統合する |
| Domain Expert | ソフト、ハード、製造、安全、法規、運用などの専門判断を行う |
| Knowledge Steward | SEグラフ、用語、DSL、正本知識、変更履歴を管理する |
| AI Agent Supervisor | AIエージェントの権限、ログ、失敗、品質、再実行を管理する |
| Verification Strategist | Verification / Validationの戦略を設計する |
| Operator / Maintainer | 運用・保守視点から安全性、実行可能性、手動代替を判断する |
| Auditor | 根拠、承認、逸脱、履歴、説明責任を監査する |

### 7.3 工程別組織から意思決定単位の組織へ

従来型の組織は工程別に分かれやすい。

```text
企画 → 要求定義 → 設計 → 実装 → テスト → 運用
```

AI時代のSEシステムでは、組織は意思決定単位に近づく。

```text
Decision Cell
  - Business Owner
  - Chief Systems Engineer
  - Domain Experts
  - V&V Strategist
  - Knowledge Steward
  - AI Agent Supervisor
  - Implementation Agents / Engineers
```

この構造では、成果物の受け渡しではなく、判断状態の収束と差分レビューが中心になる。

---

## 8. 表現言語への依存を避ける

SEシステムは、SysMLを前提にしない。SysMLは有効なビューの一つだが、正本ではない。

SEシステムは、次の形式化の階段を扱う。

```text
Level 0: 自然言語
  顧客発言、議事録、要望、背景、経営方針

Level 1: 構造化自然言語
  誰が、何を、なぜ、どの条件で、どう成功判定するか

Level 2: 準形式表現
  要求表、業務フロー、状態遷移、トレース表、判断表

Level 3: ドメイン固有言語
  安全要求DSL、業務ルールDSL、インターフェース契約DSL、検証条件DSL

Level 4: 形式言語
  制約式、時相論理、状態機械、契約仕様、モデル検査可能な仕様

Level 5: 実行・検証可能モデル
  シミュレーション、デジタルツイン、テストハーネス、コード、CI
```

形式化は常に良いとは限らない。企画や顧客価値の段階では、自然言語の曖昧さが仮説探索に役立つ。一方で、安全要求、インターフェース契約、検証条件は、必要に応じてDSLや形式仕様へ落とすべきである。

したがって、SEシステムは「何をどこまで形式化するか」をDecisionとして扱う。

---

## 9. AIコーディング、OpenClaw型自動化、SEシステムの区分

| 区分 | 主対象 | 主目的 | 成果物 | 判定基準 | 限界 |
|---|---|---|---|---|---|
| AIコーディングエージェント | コード、Issue、PR、テスト、既存リポジトリ | 実装、修正、テスト、リファクタを速くする | コード、テスト、PR、修正案 | コンパイル、テスト、lint、レビュー | 何を作るべきか、要求が妥当か、事業価値があるかは決めない |
| OpenClaw型業務エージェント | PC、ブラウザ、Slack、Discord、既存アプリ、定型作業 | 人間の操作や業務フローを自動実行する | アプリ操作、通知、スケジュール、業務処理 | タスク完了、人間確認、権限制御 | 業務は実行できるが、要求妥当性や設計判断の正本化は主目的ではない |
| SEシステム | 企画、要求、制約、運用、構造、検証、判断、根拠、専門家合意 | 何を、なぜ、どの制約で、どう検証するかを決める | Decision、Requirement、V&V、Trace、Rationale、Evidence、Org responsibility | 妥当性、追跡性、根拠、整合性、検証可能性、変更耐性 | 実装や外部ツール操作は下流実行者に渡す |

関係は次である。

```text
SEシステムが「実行してよい対象」を定義する
AIコーディングエージェントが「コードとして実行する」
OpenClaw型エージェントが「既存環境上で業務操作として実行する」
```

---

## 10. AI開発の現状から見た補強

2026年時点では、AIエージェントはコードや業務操作の実行能力を急速に伸ばしている。OpenAI Codexはクラウド上のソフトウェアエンジニアリングエージェントとして、機能実装、コードベースへの質問、バグ修正、PR提案などを行う。GitHub Copilot cloud agentはリポジトリ調査、実装計画、ブランチ上のコード変更、テスト・lint実行、PR作成を扱う。Claude Codeはコードベースを読み、ファイル編集、コマンド実行、開発ツール連携を行う。OpenClawはブラウザ、canvas、nodes、cron、sessions、Discord/Slack actions など、既存環境上で行動するツールを持つ。

この現状は、知識収束学に対して二つの修正を要求する。

第一に、AIを「候補生成・分析補助」だけでなく、**限定された実行主体**として扱う必要がある。第二に、AIが実行できるからこそ、**責任・権限・根拠・監査・停止・差戻し**をより明示的に設計する必要がある。

したがって、SEシステムでは、AIエージェントを次の四つに分類する。

| AIエージェント種別 | 役割 | 正本への扱い |
|---|---|---|
| Candidate Agent | 要求候補、論点候補、設計案候補を出す | 候補。人間承認まで正本ではない |
| Critique Agent | 矛盾、曖昧性、抜け漏れ、リスクを指摘する | 検査結果。根拠参照が必要 |
| Execution Agent | コード、テスト、資料、業務操作を実行する | 委任された実行。ログと差分が必須 |
| Guardian Agent | 他エージェントの権限、リスク、ルール逸脱を監視する | 監査支援。最終責任主体ではない |

---

## 11. 理論基盤への補強原則

既存の知識収束学の中核は妥当である。ただし、SEシステム統合では次の原則を追加採用する。

### P-SE1: SE収束は実装可能性だけでなく妥当性確認へ接続する

Verification passed は Validation passed を意味しない。テストが通っても、顧客価値や運用目的を満たすとは限らない。

### P-SE2: AIの実行権限と結果責任を分離する

AIは実行主体になれる。しかし、AIは既定の結果責任主体ではない。AIに委任する場合、委任範囲、権限、ログ、停止条件、レビューゲートを明示する。

### P-SE3: 組織と人間系は外部環境ではなくシステム要素である

役割、権限、専門性、訓練状態、認知負荷、停止権、手動代替は、SEシステム内の管理対象である。

### P-SE4: 表現形式は正本ではなくビューである

自然言語、SysML、UML、BPMN、DSL、形式仕様、コードは、正本知識の異なる投影である。正本は、根拠付きの意味中間表現である。

### P-SE5: AI時代の組織は工程別ではなく意思決定単位で設計する

AIが実装と業務実行を加速するほど、人間組織は「成果物を作る組織」から「判断状態を収束させる組織」へ移る。

---

## 12. 最小MVP

SEシステムのMVPは、万能AIエージェントでもSysMLエディタでもない。最初に作るべきものは次の五つである。

### 12.1 Evidence-backed Decision Ledger

```text
Issue
Option
Criteria
Decision
Rationale
Evidence
Assumption
Rejected option
Reopen condition
Responsible role
```

### 12.2 Requirement / Validation / Verification Graph

```text
Need
Operational Scenario
Requirement
Verification Method
Validation Scenario
Evidence
```

### 12.3 SE Lint

```text
根拠なし要求
検証不能要求
Validation未接続要求
根拠なしDecision
却下案なしDecision
AI委任権限なし実行
人間停止権なし高リスク実行
変更影響未評価
```

### 12.4 Organization / Human Packet

```text
Role
Expertise scope
Decision right
Approval rule
Training readiness
Override right
Manual fallback
Escalation path
```

### 12.5 Agent Delegation Packet

```text
Agent identity
Capability scope
Authority envelope
Sandbox policy
Input knowledge refs
Output artifact refs
Audit logs
Human review gate
Rollback path
```

---

## 13. 成功指標

SEシステムの成功指標は、AIが何件生成したかではない。

見るべき指標は次である。

- 根拠なし要求が減ったか
- 検証不能要求が減ったか
- Validation未接続要求が減ったか
- 変更影響分析の時間が減ったか
- 設計判断の根拠再利用率が上がったか
- 専門家間の未解決対立が可視化されたか
- AIエージェントの無権限実行が減ったか
- 手戻りが減ったか
- 運用フィードバックから要求・設計のreopenが起きるようになったか
- 人間が停止・差戻し・再判断できる状態が保たれたか

---

## 14. 非目標

この annex は、次を目標にしない。

- SysMLを唯一の前提にすること
- AIに最終責任を持たせること
- すべての意思決定を自動化すること
- 万能スコアでトレードオフを一発解決すること
- 人間承認を形式的なボタン操作にすること
- 組織の価値衝突を隠して単一結論へ圧縮すること

---

## 15. まとめ

知識収束学は、「生成物を知識にする条件」を扱う。SEシステムは、その条件をシステム開発に適用する。

AI時代には、コードを書く能力と業務を実行する能力は急速に拡大する。しかし、何を作るべきか、なぜ作るべきか、どの専門家の判断をどう統合するか、どの条件で成功とみなすか、誰が責任を持つかは、コード生成だけでは解けない。

したがって、SEシステムの本質は次である。

> **SEシステムは、AIエージェント時代における、事業・組織・人間・技術・検証を接続する知識収束基盤である。**

---

## 参考文献・参照元

- ISO/IEC/IEEE 15288:2023, Systems and software engineering — System life cycle processes  
  https://standards.ieee.org/ieee/15288/10424/
- SEBoK, Systems Engineering Overview  
  https://sebokwiki.org/wiki/Systems_Engineering_Overview
- NASA Systems Engineering Handbook, Appendix definitions of Product Verification / Product Validation  
  https://www.nasa.gov/reference/system-engineering-handbook-appendix/
- NIST AI Risk Management Framework  
  https://www.nist.gov/itl/ai-risk-management-framework
- OpenAI, Introducing Codex  
  https://openai.com/index/introducing-codex/
- GitHub Docs, About GitHub Copilot cloud agent  
  https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent
- Anthropic, Claude Code overview  
  https://code.claude.com/docs/en/overview
- OpenClaw GitHub repository  
  https://github.com/openclaw/openclaw
- McKinsey, The state of AI in 2025: Agents, innovation, and transformation  
  https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
- BCG, How Agentic AI is Transforming Enterprise Platforms  
  https://www.bcg.com/publications/2025/how-agentic-ai-is-transforming-enterprise-platforms
- Deloitte, Rethinking operating models for humans with agents  
  https://www.deloitte.com/us/en/insights/topics/talent/operating-models-for-humans-ai-agents.html
- Deloitte, AI and the future of human decision making  
  https://www.deloitte.com/us/en/insights/topics/talent/human-capital-trends/2026/decision-making-with-ai.html


---

## 追補 v1.1: core側への昇格

前版では、SEシステム向けの「工学的妥当性収束」は `10_se_system_annex` 内の追加条件として扱った。v1.1 ではこの弱点を修正し、core 側に汎用の `domain_validity_convergence` を追加した。

SEシステムでは、`domain_validity_convergence` を `engineering_validity_convergence` として具体化する。つまり、認識収束と統治収束だけではなく、次も満たす必要がある。

```text
Requirement / Constraint / Decision
→ Verification
→ Validation
→ Intended environment
→ Human / organization readiness
→ Operational feedback
→ Reopen / revalidate / rollback
```

この変更により、`承認されたが妥当性確認されていない`、`テストは通ったが顧客価値を満たしていない`、`AIが実行できるが人間・組織が監督できない` という状態を、core の不適合または hold として扱える。

# 現在のAI開発状況に関する参照メモ v1

作成日: 2026-05-08  
目的: SEシステム統合 annex で参照した、AIコーディング、業務実行エージェント、組織変化に関する外部参照を整理する。

---

## 1. AIコーディングエージェント

### OpenAI Codex

OpenAI は Codex をクラウド型ソフトウェアエンジニアリングエージェントとして説明している。Codex は、機能実装、コードベースへの質問、バグ修正、レビュー用PR提案を行う。

参照:
- https://openai.com/index/introducing-codex/
- https://openai.com/codex/

### GitHub Copilot cloud agent

GitHub Copilot cloud agent は、リポジトリ調査、実装計画、ブランチ上のコード変更、テスト・lint実行、PR作成を扱う。

参照:
- https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent

### Claude Code

Claude Code は、コードベースを読み、ファイル編集、コマンド実行、開発ツール連携を行う agentic coding tool として説明されている。

参照:
- https://code.claude.com/docs/en/overview

---

## 2. OpenClaw型の業務実行エージェント

OpenClaw は、ブラウザ、canvas、nodes、cron、sessions、Discord/Slack actions などのツール群を持つAIアシスタントとして説明されている。GitHub README では、サンドボックス既定設定として許可・拒否ツールの例も示されている。

参照:
- https://github.com/openclaw/openclaw
- https://openclaw.ai/

---

## 3. AIエージェント導入と組織変化

### McKinsey

McKinsey の 2025 年 AI 調査は、AI利用が一般化している一方で、企業全体の価値獲得はまだ途上であり、AI高業績企業はワークフロー再設計とリーダー関与を進めていると述べている。

参照:
- https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
- https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/the-agentic-organization-contours-of-the-next-paradigm-for-the-ai-era

### BCG

BCG は、agentic AI を安全・信頼可能に拡張するには、AI自律性と人間監督のバランス、価値連鎖全体にわたる制御、ワークフロー・ガバナンス・役割・投資の再設計が必要だと述べている。

参照:
- https://www.bcg.com/publications/2025/how-agentic-ai-is-transforming-enterprise-platforms
- https://www.bcg.com/publications/2025/machines-that-manage-themselves
- https://www.bcg.com/publications/2026/rebuilding-asset-management-for-an-ai-first-world

### Deloitte

Deloitte は、エージェントを既存の人間向け業務モデルへ単に載せるだけでは不十分であり、仕事・意思決定権・リスク責任・品質保証・人間の役割を再設計する必要があると述べている。また、人間とAIが関わる意思決定では、責任連鎖、AI監督、ヒューマンエージェンシーを設計する必要がある。

参照:
- https://www.deloitte.com/us/en/insights/topics/talent/operating-models-for-humans-ai-agents.html
- https://www.deloitte.com/us/en/insights/topics/talent/human-capital-trends/2026/decision-making-with-ai.html

### Gartner

Gartner は、agent sprawl に対して、agent governance、centralized agent inventory、agent identity / permission / lifecycle model、AI information governance を示している。

参照:
- https://www.gartner.com/en/newsroom/press-releases/2026-04-28-gartner-identifies-six-steps-to-manage-artificial-intelligence-agent-sprawl

---

## 4. SEシステム統合への含意

これらの参照から、SEシステム統合では次を補強する。

1. AIは候補生成だけでなく実行主体になりうる。
2. 実行主体になれることと、結果責任を持てることは別である。
3. コード生成や業務操作の前に、Decision、V&V、組織責任、権限、根拠を収束させる必要がある。
4. AIエージェントの導入は、ツール導入ではなく、ワークフロー、組織構造、意思決定権、監督、監査、役割の再設計を伴う。
5. SEシステムは、AIエージェント群を下流実行者として統制するための Convergence / Governance plane を提供する。

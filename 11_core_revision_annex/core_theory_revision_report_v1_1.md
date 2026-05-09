# 知識収束学 core 理論改訂レポート v1.1

作成日: 2026-05-08

## 1. 改訂の結論

v1 の理論基盤は、SEシステムの基礎として有効である。ただし、AIエージェントが実行主体化し、システム開発の上流意思決定・V&V・組織責任まで扱うには、二層収束だけでは弱い。

そのため v1.1 では、core に第三層として `domain_validity_convergence` を追加した。

```text
認識収束: 内容として説明できるか
統治収束: 誰がどの条件で実行・保留・差戻しできるか
ドメイン妥当性収束: 対象ドメインで実際に使ってよいか
```

SEシステムでは、第三層を `engineering_validity_convergence` として扱う。

## 2. 修正した弱点

### 2.1 二層収束だけでは「承認されたが妥当ではない」を扱いにくい

認識収束と統治収束が成立しても、対象ドメインでの妥当性が未成立の場合がある。

例:

- 仕様は説明でき、承認もされたが、Validation scenario がない。
- テストは通ったが、実運用環境で顧客価値を満たすか不明である。
- AIがコードを修正できるが、システム要求・安全要求・変更影響に接続されていない。

これを扱うため、`domain_validity_convergence` を追加した。

### 2.2 AIを候補生成者だけとして扱うと現状に合わない

AIエージェントは、すでにコード編集、テスト実行、PR作成、外部ツール操作を行う。したがって、AIを単なる候補生成者ではなく、限定された実行主体として扱う必要がある。

v1.1 では、`agent_execution_governance` と `agent_execution_envelope` を追加した。

### 2.3 human-in-the-loop は安全性を自動保証しない

人間が形式的に承認欄に入っていても、説明を理解できず、停止権もなく、時間的余裕もなく、訓練も不十分であれば、実質的な監督ではない。

v1.1 では、`meaningful_human_oversight` を追加した。

### 2.4 組織構造が外部条件のままだとSEシステムに弱い

SEシステムでは、組織構造、人間の役割、専門性、意思決定権、サプライヤー境界、レビュー能力がシステム成立性に直結する。

v1.1 では、`organization_topology` を追加した。

### 2.5 収束状態を単一スコアにすると blocker が隠れる

高い平均点で validation blocker や authority gap を相殺してはいけない。

v1.1 では、`convergence_measurement` と blocker-preserving aggregation を追加した。

## 3. SEシステムへの効果

この改訂により、SEシステムは次を core 準拠で扱える。

- コードを書く前の意思決定
- Requirement / Verification / Validation の接続
- 人間・組織・専門家・サプライヤー境界
- AIエージェントの実行委任
- 運用フィードバックからの reopen / revalidate / rollback
- 収束状態の多次元計量

## 4. 互換性

`K=(G,C,E,V,R,H)` は維持する。既存の二層モデルは廃止せず、後方互換の中核として残す。v1.1 は、その上に domain validity layer と関連 packet を追加する。

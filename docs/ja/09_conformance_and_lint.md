# 適合検査とLint

知識収束学は、曖昧なスローガンに留まるべきではありません。検査可能であるべきです。

このリポジトリには、知識状態が必要条件を満たしているかを確認するためのschema、profile、rulebook、test vector、exampleを含みます。

## なぜ適合検査が重要か

適合規則がなければ、重要条件が欠けていても「知識は収束した」と主張できてしまいます。

適合検査は、次を検出します。

- 根拠不足
- 文脈不足
- オーナー不在
- 権限包絡不足
- 妥当性確認不足
- ロールバック経路不足
- 形式的な人間承認
- 未レビューのAI実行
- 平均スコアに隠れたblocker

## Lintの考え方

Lint規則は、問題全体を解く必要はありません。レビューすべき条件を検出します。

例:

```text
KC-LINT-REQ-001: Requirement has no linked evidence.
KC-LINT-REQ-002: Requirement has no validation scenario.
KC-LINT-DEC-001: Decision has no accountable owner.
KC-LINT-AGENT-001: Agent action has no authority envelope.
KC-LINT-AGENT-002: Agent action has no rollback path.
KC-LINT-HUMAN-001: Human approval lacks stop authority.
```

## SE Lintの例

システムズエンジニアリングでは、次の検査が有効です。

- ステークホルダニーズに紐づかない要求
- 検証方法のない要求
- 検証はあるが妥当性確認がない要求
- 理由のない判断
- 却下案のないトレードオフ
- 影響分析のない変更
- 承認済み要求のないAIコーディングタスク
- ロールバック経路のない高リスク操作

## Blocking logic

平均は危険です。多くの次元で高スコアでも、blocker が一つあれば知識状態は実行不可です。

例:

```text
evidence = high
context = high
owner = present
validation = missing
agent rollback path = missing
```

この場合、正しい分岐は hold かもしれません。

## 適合検査の利用場面

適合検査は次で使えます。

- レビューゲート
- CIパイプライン
- AIエージェント委任ゲート
- SEモデルレビュー
- 要求レビュー
- 変更承認会議
- 監査ワークフロー

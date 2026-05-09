# 例

この文書では、簡単な例をまとめます。詳細な例は [`../../examples/public/ja/`](../../examples/public/ja/) にあります。

## 1. 材質変更が妥当性確認不足で hold になる

チームがコスト削減のために材質変更を提案します。

提案にはコスト効果と初期実現性があります。しかし、安全性の妥当性確認とサプライヤ影響レビューが不足しています。

結果:

```text
outcome = hold
reason = validation evidence and supplier review are missing
```

参照: [`material_change_hold.md`](../../examples/public/ja/material_change_hold.md)

## 2. AIコーディング委任が権限包絡不足で hold になる

チームがAIコーディングエージェントに変更実装を依頼します。

実装対象は明確ですが、リポジトリ権限、レビューゲート、ロールバック経路が定義されていません。

結果:

```text
outcome = hold
reason = missing agent execution envelope
```

参照: [`ai_coding_delegation.md`](../../examples/public/ja/ai_coding_delegation.md)

## 3. 検証は通ったが妥当性確認が失敗した

要求は検証テストに合格しました。しかし、運用シナリオではユーザーワークフローが依然として遅いことが分かりました。

結果:

```text
verification_status = pass
validation_status = fail
outcome = reopen
```

参照: [`requirement_validation_gap.md`](../../examples/public/ja/requirement_validation_gap.md)

## 4. 組織のレビュー能力不足

高リスク判断がドメイン専門家に回されます。その専門家は能力を持っていますが、リリースゲート前に十分なレビュー時間を確保できません。

結果:

```text
outcome = escalate
reason = review capacity gap for high-risk decision
```

参照: [`organization_capacity_gap.md`](../../examples/public/ja/organization_capacity_gap.md)

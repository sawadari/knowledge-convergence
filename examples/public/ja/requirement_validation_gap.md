# 例：検証は通ったが妥当性確認が不足している

## 状況

要求は次のように書かれています。

```text
システムはタスク登録を2秒以内に完了しなければならない。
```

テストは合格しました。システムは登録を2秒以内に完了します。

しかし、運用シナリオでは、利用者はそのタスクを何度も繰り返す必要があり、ワークフロー全体は依然として遅いと感じます。

## 区別

| 項目 | 結果 |
|---|---|
| Verification | pass |
| Validation | fail |

## 知識収束結果

```text
verification_status = pass
validation_status = fail
outcome = reopen
reason = intended operational use is not satisfied
```

## 教訓

指定されたテストに合格することと、意図した利用を満たすことは同じではありません。

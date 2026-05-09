# 基礎発展 annex リリースノート v1

## この段階で足したもの
- 発話解釈のための `KC-L1`
- 競合意味論のための `KC-M1`
- 多基準判断のための `KC-M2`
- 由来・時相保証のための `KC-M3`

## 設計上の判断
- `K = (G, C, E, V, R, H)` 自体は維持
- 上流 packet と下流 packet を追加し、core へ無理に詰め込まない
- 既存の hold / branch / approval / audit と矛盾しないよう addendum 化
- `01_core` には discoverability のための profile と contract addendum だけを置く

## 期待効果
- claim 抽出時の過剰断定を減らす
- H2 の説明粒度を上げる
- V の単一スコア偏重を避ける
- rollback / expiry / reapproval を追いやすくする

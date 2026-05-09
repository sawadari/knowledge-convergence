# 制度運用発展 annex リリースノート v1

## この段階で足したもの
- 証言と正当化のための `KC-T1`
- 合議と集約のための `KC-S1`
- ライフサイクル運用のための `KC-O1`
- 人間中心監督のための `KC-H1`

## 設計上の判断
- `K = (G, C, E, V, R, H)` 自体は維持
- core と foundational を上書きせず、制度運用 packet を追加
- vote count や expert label を真理や authority の代替にしない
- execute / hold / rollback などの branch 語彙は維持し、その周辺の justification・gate・fallback を増設

## 期待効果
- 証言の扱いが source quality の一語から脱却する
- group outcome に aggregation rule と dissent が残る
- decision outcome が baseline / gate / artifact と接続される
- 人の停止権・訓練完了・手動代替が lawful state として扱える


## 次段での接続
この版で追加した packet 群は、次段の `09_conformance_suite/` で検査可能な rule id と test case に接続される。  
つまり institutional annex は語彙層、conformance suite は検査層として位置づく。

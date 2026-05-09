# 制度運用発展 annex 導入ロードマップ

## Phase 1: 証言を source quality から justification へ上げる
対象:
- 専門家レビューや監査済み記録をよく使う実装
- 伝聞や代理報告を support として多用する実装

採用:
- `KC-T1`
- `epistemic_justification_packet`
- `defeater_register`

成果:
- 「誰が言ったか」だけでなく
- 「どの範囲まで信じてよいか」
- 「何がそれを弱めるか」
を保持できる。

## Phase 2: 複数レビューを合議として閉じる
対象:
- 複数承認者や委員会レビューがある
- majority の説明責任が弱い
- dissent を残したい

採用:
- `KC-S1`
- `aggregation_rule_profile`
- `minority_report_packet`

成果:
- outcome がどのルールから出たか説明できる。
- premise inconsistency を silent flatten しにくくなる。

## Phase 3: decision outcome を運用成果物へ接続する
対象:
- release / deployment / rollback / handoff を扱う
- execute を runbook や training と結び付けたい
- incident から reopen を起こしたい

採用:
- `KC-O1`
- `lifecycle_gate_packet`
- `ops_feedback_event`

成果:
- branch が gate / baseline / artifact と接続される。
- incident を lawful recovery loop へ戻せる。

## Phase 4: 人が安全に止められる状態を作る
対象:
- 現場運用者が system output を扱う
- stop right や fallback の有無が重要
- training 完了や operator acceptance を追いたい

採用:
- `KC-H1`
- `human_oversight_packet`
- `manual_fallback`

成果:
- 人の停止権・引継ぎ・手動代替が state として管理できる。
- 説明の粒度を role ごとに分けられる。

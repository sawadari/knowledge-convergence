# 基礎発展用語集 addendum

## Utterance Interpretation Envelope
自然言語の発話を、そのまま claim に潰さずに保持する上流 packet。  
最低でも `speech_act`、`speaker_commitment`、`evidentiality`、`deictic_anchor` を持つ。

## Speech Act
発話が「断定」「質問」「指示」「報告」「提案」のどれに属するかを表す型。

## Speaker Commitment
話者が内容にどの程度コミットしているかを表す型。  
例: `asserted_strong`, `hedged`, `attributed`, `hypothetical`

## Evidentiality
その内容が直接観測・推論・伝聞・仮定のどれに近いかを表す型。

## Presupposition
明示的に主張されていないが、発話が成り立つために前提化されている内容。

## Deictic Anchor
誰が・いつ・どの範囲で・何を指して述べたかを定める文脈アンカー。

## Claim Kind
claim の存在論的な型。  
例: `fact`, `event`, `state`, `norm`, `plan`, `report`, `obligation`

## Ambiguity Profile
曖昧性をひとまとめにせず、参照・scope・modality・presupposition・談話関係・gradable threshold などに分けて保持する packet。

## Four-Valued Support Status
`supported`, `refuted`, `both`, `neither` の4値で支持関係を保持する方法。

## Argument Graph
主張どうしの support / rebut / undercut / priority 関係を明示したグラフ。

## Outranking
単一スコアに潰さず、`A が B を上回る`, `比較不能`, `veto で失格` などを扱う多基準判断の型。

## Measurement Profile
ある quantity や score が順序尺度・間隔尺度・比尺度のどこまで意味を持つかを固定する profile。

## Provenance Trace
どの入力・変換・承認・反証・差戻しを経て現在の state に至ったかを追跡する由来情報。

## Temporal Guard
approval や hold が、いつ発効し、いつ失効し、どのイベントで更新されるかを表す時間拘束 packet。

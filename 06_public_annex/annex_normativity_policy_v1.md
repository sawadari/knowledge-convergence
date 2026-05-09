# 公開 annex の規範性ポリシー

## 優先順位
1. `01_core/`  
   公開仕様の canonical public contract です。
2. `06_public_annex/`  
   公開配布面として再編集した補助規則です。
3. `02_supplements/`  
   研究由来の raw supplement です。

## annex の役割
annex は、`01_core/` だけでは判断粒度が荒くなりやすい論点に対して、
- 用語を増やしすぎず
- 実装面の touchpoint を明示し
- raw supplement より短く
公開配布しやすい形に縮約したものです。

## annex の読み方
- `recommended_extension`  
  公開実装・対外レビュー・仕様策定で採用を推奨する補助項目です。
- `informative_annex`  
  参照価値は高いが、初期導入で必須化しない補助項目です。

## 互換性ルール
- annex は `01_core/canonical_public_data_contract_v1.yaml` の必須語彙を壊してはならない
- annex は `01_core/json_schema/` の最小互換性を壊してはならない
- annex により追加される細目は、拡張フィールドか別 registry として表す
- annex が拾わなかった詳細は `02_supplements/` を source of detail とする

## annex を使う場面
- public spec に weighted quorum や hold taxonomy の補助説明を足したい
- 監査ログ・匿名化・bounded summary を対外資料へ載せたい
- authority tier や deadline の説明を、研究本文より短く配布したい

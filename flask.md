# FLaskとは

- Pythonで利用されるWebフレームワーク
- MVT（モデル・ビュー・テンプレート）と呼ばれる考え方でコードを作成する

> Model DBへアクセスし、データ操作(insert,update,select)  
> View 入力を受けてModelを呼び出す、取得したデータをTemplateを返す  
> Template 動的ページ

<!-- TODO make it flow -->
CS / BS flow
C/B (user) -> S View -> Model ->DB
                View <- Model <-DB
                   ↓
C/B (user) <- S Template / api

## ルーティング

- 静的ルーティング
- 動的ルーティング

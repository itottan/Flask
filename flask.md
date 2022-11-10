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

## form[画像のアップロード]

```html
    <form method="POST" enctype="multipart/form-data"></form>
```

```py
    # flask
    file = request.files['file']

    # fileName を適切な形に変換する
    # 日本語対応するには追加のLbが必要 ~ pip i pykakasi
    save_filename = secure_filename(file.filename) 
    file.save(file_path)
```

werkzeug[ヴェルクツォイク]
> WSGIユーティリティライブラリ  
> [ Web Server Gateway Interface utility library ]  

WebServer <> AppServer 間の接続するためのインタフェース。

### pykakasi 日本語をアルファベットへ変換用Lb

依頼を追加手順:

  1. condaの開発環境を選択 `conda activate 'envNm'`
  2. pykakasi をインストール`pip install pykakasi`
  3. .py にimport

設定：

- k.setMode('H', 'a') # ひらがな → hiragana
- k.setMode('K', 'a') # カナ → kana
- k.setMode('J', 'a') # 漢字 → kanji

conv = k.getConverter()
conv.do(val) # あ → a 日本 → nippon

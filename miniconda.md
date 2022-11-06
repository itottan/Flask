# miniconda コマンドメモ

目的：pythonの開発環境構築
  miniconda(free) & anaconda(有料)
  > Django, Flask: AppServerSideDevelop **[WebApp開発用]**
  > Tensorflow, Scikit-learn AIDev

- 仮想環境の作成
  - 環境一覧
    - `conda env list`
  - 新規python3.10環境作成 / 削除
    - `conda creat -n 'EnvName' python= 3.10`
    - `conda remove -n 'EnvName' --all [option]`
  - 指定の環境をアクティブ化 / 終了
    - `conda activate 'EnvName'`
    - `conda deactivate`
  - ライブラリ一覧 / インストール / 削除
    - `conda list`
    - `conda install django`
    - `conda remove django`
- `conda activate -> CommandNotFoundError` 
  - 以下のCmdを入力し`conda init / conda init zsh` ターミナルを再起動
  - 原因ぽいのはcondaの更新や環境構築後正しいinitできなかったみたい
  
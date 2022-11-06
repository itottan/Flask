#! /usr/local/Caskroom/miniconda/base/envs/flaskenv/bin/python python3
# -*- coding: utf-8 -*-

#render_templateは出力したいHtmlファイルを指定したい場合の追加機能
from flask import Flask, render_template, redirect, url_for, abort
# from flask import Flask, render_template ,request, redirect, url_for, abort

# app = Flask(__name__, template_folder='customize_tpl_folder') #テンプレートフォルダーを別に指定したい場合　デフォルトはtemplates
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/home/<string:user_name>/<int:age>')
# def home(user_name, age):
#     # login_user = user_name 
      # dictを戻す
#     login_user = { 
#       'name': user_name,
#       'age': age
#     }
#     # return (遷移先のHtml,　第二引数を渡したいパラメーターを渡す)
#     # return render_template('home.html', login_user=login_user) 
#     return render_template('home.html', user_info=login_user) 

# 一時テスト用UsersList
users = ['user1, user2, user3']
@app.route('/user/<string:user_name>/<int:age>')
def user(user_name, age):
    if user_name in users:
        # リダイレクトコード: 302 を戻す
        return redirect(url_for('home', user_name=user_name, age=age))
    else:
        abort(500, 'インタネットサーバーエラー:該当するユーザーが存在しません。')


@app.route('/home')
def home():
  # print(request.full_path)
  # print(request.method)
  # print(request.args)
  return render_template('home.html')

@app.route('/signup')
def sign_up():
    return render_template('signup.html')

# 追加したいフィルターの作成 [customizeFilterの作成する場合]
@app.template_filter('customize_filter') 
def my_filter_fn(s):
    # return 'xxx'  #戻り値を設定
    # pass

    #値を逆転 ※iterable[イテラブル]] can be slice[スライス]
    #イテレータ(iterator) は『イテラブルなオブジェクト』の中の1つでイテレーションした状態を記憶しておくことができるオブジェクト（イテレータ型のオブジェクト）です。
    return s[::-1] 

# Err制御
@app.errorhandler(500)
def system_error(error):
    #　abortからthrowされたエラーメッセージを保存
    error_description = error.description
    return render_template('system_error.html', error_description=error_description), 500

@app.errorhandler(404)
def page_not_fount(error):
    # コード404の場合、NotFoundページへ遷移し、404コードを戻す
    return render_template('not_found.html'), 404


if __name__ == '__main__': #TODO if文にした原因
    app.run(debug=True) #開発モード用、動的コンパイル
    # app.run()
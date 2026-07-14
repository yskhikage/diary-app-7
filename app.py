from dotenv import load_dotenv
#環境変数読み込み
load_dotenv()


from flask import Flask, render_template, url_for, redirect, session,request
from flask_sqlalchemy import SQLAlchemy
from form import RegistrationForm
from datetime import datetime
from flask_wtf import FlaskForm





app = Flask(__name__)
#設定読み込み
app.config.from_object('config')


#DBを作成してからモデルを読み込む
db = SQLAlchemy(app) 
from models import Event


#SessionClass = sessionmaker(db)  # セッションを作るクラスを作成
#session = SessionClass()


@app.route('/')
def idnex():
    return "Hello,Flask"

#events = [
    #{
        #'title': 'event1',
        #'date': '2026-07-15'
    #},
    #{
        #'title': 'event2',
        #'date': '2026-07-20'
    #}
#]

@app.route('/calendar')
def calender():
#DB取得
    events = Event.query.all()
    return render_template('calendar.html',events=events)


#各ページごとのルーティング
@app.route('/calendar/<int:id>')
def calendar_id(id):
    one_event = Event.query.get_or_404(id)
    return render_template('detail.html',one_event=one_event)


#追加
@app.route("/register", methods=["GET", "POST"])
def register():
    #フォームを取得
    form = RegistrationForm()
    #フォームにデータ入力されていれば、入力チェック
    if form.validate_on_submit():
        print('フォームを受け取り')
        #フォーム情報をセッションに格納
        name = form.name.data
        date = form.date.data
        print(name,date)
        event = Event(name=name,date=date,created_at=datetime.now())
        db.session.add(event)
        db.session.commit()
        #カレンダーに
        return redirect(url_for("calender"))
    #フォームにはデータが入力されていない状態だと、if文の中は処理されず、登録ページを表示する
    print('formを受け取れてないっすね')
    return render_template("register.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
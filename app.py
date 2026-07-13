from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy 
from requests import request


app = Flask(__name__)
app.config.from_object('config')

#DBを作成してからモデルを読み込む
db = SQLAlchemy(app) 
from models import Event


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


if __name__ == '__main__':
    app.run(debug=True)
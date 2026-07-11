from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def idnex():
    return "Hello,Flask"

events = [
    {
        'title': 'event1',
        'date': '2026-07-15'
    },
    {
        'title': 'event2',
        'date': '2026-07-20'
    }
]

@app.route('/calender')
def calender():
    return render_template('calendar.html',events=events)

if __name__ == '__main__':
    app.run(debug=True)
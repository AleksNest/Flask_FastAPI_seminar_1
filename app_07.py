from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/news/')
def news():

    context = [
        {'name': 'Наука и техника' },
        {'description':
             'Ученые из Техасского университета и организации Sandia впервые выявили у металлов '
             'способность к самовосстановлению. Использование этого механизма позволит разработать '
             'самовосстанавливающиеся двигатели, мосты и самолеты, сократив их износ. '
             'Результаты исследования опубликованы в журнале Nature.'
         },
        {'date': '23-07-2023',
         }
    ]
    return render_template('news.html', news=context)



if __name__ == '__main__':
    app.run()
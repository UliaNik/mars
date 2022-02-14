from flask import Flask
from flask import url_for, request

app = Flask(__name__)


@app.route('/')
@app.route('/sample_page')
def return_sample_page():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Марс</title>
                  </head>
                  <body>
                    <h1>Миссия Колонизация Марса</h1>
                  </body>
                </html>"""


@app.route('/index')
def index():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Марс</title>
                      </head>
                      <body>
                        <h1>И на Марсе будут яблони цвести!</h1>
                      </body>
                    </html>"""


@app.route('/promotion')
def promotion():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Марс</title>
                      </head>
                      <body>
                        <br>Человечество вырастает из детства.</br>
                        <br>Человечеству мала одна планета.</br>
                        <br>Мы сделаем обитаемыми безжизненные пока планеты.</br>
                        <br>И начнем с Марса!</br>
                        <br>Присоединяйся!</br>
                      </body>
                    </html>"""


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.jpg')}" 
           alt="нет марса(">
                      </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
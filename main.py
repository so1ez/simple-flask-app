from datetime import datetime

from flask import Flask, render_template

from settings import SETTINGS


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           name = SETTINGS.NAME,
                           time_passed = (datetime.now() - datetime(SETTINGS.BIRTHDAY_YEAR,
                                                                    SETTINGS.BIRTHDAY_MONTH,
                                                                    SETTINGS.BIRTHDAY_DAY)).days)

def main() -> None:
    app.run(host='127.0.0.1', port=8000)

if __name__ == '__main__':
    main()
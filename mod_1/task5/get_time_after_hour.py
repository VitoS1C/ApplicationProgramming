from flask import Flask
from datetime import datetime, timedelta

app = Flask(__name__)


@app.route('/get_time/future')
def get_time_after_hour():
    current_time_after_hour = (datetime.now() + timedelta(hours=1)).strftime('%H:%M:%S')
    return f"Точное время через час будет {current_time_after_hour}"

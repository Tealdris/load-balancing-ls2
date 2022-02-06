from flask import request, Flask
import json
import time
from datetime import datetime

app1 = Flask(__name__)


@app1.route('/')
def hello_world():
    date = datetime.now()
    return (date.strftime("%d/%m/%y"))


if __name__ == '__main__':
   app1.run(debug=True, host='0.0.0.0')

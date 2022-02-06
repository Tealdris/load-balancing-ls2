from flask import request, Flask
from datetime import datetime
import json
import time

app1 = Flask(__name__)


@app1.route('/')
def hello_world():
    date = datetime.now()
    return (str(datetime.now()))


if __name__ == '__main__':
   app1.run(debug=True, host='0.0.0.0')

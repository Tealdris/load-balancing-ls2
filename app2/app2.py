from flask import request, Flask
import json
import datetime

app1 = Flask(__name__)


@app1.route('/')
def hello_world():
    return ('Hello to SNE family! Time is: ')


if __name__ == '__main__':
   app1.run(debug=True, host='0.0.0.0')

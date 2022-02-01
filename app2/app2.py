from flask import request, Flask
import json
import netifaces as ni

app1 = Flask(__name__)


@app1.route('/')
def hello_world():
    ni.ifaddresses('ens3')
    ip = ni.ifaddresses('ens3')[ni.AF_INET][0]['addr']
    return 'ip'


if __name__ == '__main__':
   app1.run(debug=True, host='0.0.0.0')

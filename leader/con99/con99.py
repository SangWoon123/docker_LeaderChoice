import requests
from flask import Flask
app = Flask(__name__)


@app.route('/con99')
def con():
    token = 99
    token = requests.get('http://con_25:5000/'+str(token))
    if (token.text == "리더노드선출완료"):
        return "리더노드 99"
    con132 = requests.get('http://con_132:5003/con132')
    return con132.text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)

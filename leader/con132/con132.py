import requests
from flask import Flask
app = Flask(__name__)


@app.route('/con132')
def con():
    token = 132
    token = requests.get('http://con_25:5000/'+str(token))
    if (token.text == "리더노드선출완료"):
        return "리더노드 132"
    con232 = requests.get('http://con_232:5004/con232')
    return con232.text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003, debug=True)

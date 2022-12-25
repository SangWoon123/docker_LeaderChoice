import requests
from flask import Flask
app = Flask(__name__)


@app.route('/con232')
def con_tf():
    token = 232
    token = requests.get('http://con_25:5000/'+str(token))
    if (token.text == "리더노드선출완료"):
        return "리더노드 232"
    con54 = requests.get('http://con_54:5005/con54')
    return con54.text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004, debug=True)

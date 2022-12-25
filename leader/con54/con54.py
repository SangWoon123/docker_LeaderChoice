import requests
from flask import Flask
app = Flask(__name__)


@app.route('/con54')
def con_tf():
    token = 54
    token = requests.get('http://con_25:5000/'+str(token))
    if (token.text == "리더노드선출완료"):
        return "리더노드 54"
    return token.text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005, debug=True)

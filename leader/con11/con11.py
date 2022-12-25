import requests
from flask import Flask
app = Flask(__name__)


@app.route('/con11')
def con():
    token = 11
    token = requests.get('http://con_25:5000/'+str(token))
    if (token.text == "리더노드선출완료"):
        return "리더노드 25"
    con99 = requests.get('http://con_99:5002/con99')
    return con99.text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)

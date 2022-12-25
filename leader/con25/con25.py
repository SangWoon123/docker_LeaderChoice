import requests
from flask import Flask
app = Flask(__name__)

token = 25  # 25 컨테이너는 전역변수로 비교해준다


@app.route('/<value>')
def num(value):
    global token

    if int(value) > token:  # 첫 턴에 여기에서 비교
        token = int(value)
# ---------------파일로그 저장-----------------
        f = open('log.text', 'a')
        f.write("con"+value+"토큰과 비교후 최대값: "+str(token)+"\n")
        f.close()
# --------------------------------------------
        return str(token)
    elif int(value) == token:  # 두번째 턴에서 여기에서 비교
        token = 25  # 페이지 새로고침시 token을 초기화해준다
        return "리더노드선출완료"
    return str(token)


@app.route('/con25')
def con():
    # ---------------파일로그 저장-----------------
    f = open('log.text', 'a')
    f.write("con25 start!\n")
    f.close()
    # --------------------------------------------

    # 첫번쨰 도는 코드
    con11 = requests.get('http://con_11:5001/con11')

    # ---------------파일로그 저장-----------------
    f = open('log.text', 'a')
    f.write("한바퀴 돌고 선정된 리더 token: "+str(con11.text)+"\n")
    f.close()
    # --------------------------------------------

    # 두번째 도는 코드
    con11 = requests.get('http://con_11:5001/con11')

    # ---------------파일로그 저장-----------------
    f = open('log.text', 'a')
    f.write("두바퀴 최종 선정된 리더 token: "+str(con11.text)+"\n")
    f.close()
    # --------------------------------------------

    return "두바퀴 최종 선정된 리더 token: "+con11.text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

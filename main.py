from flask import Flask

app = Flask("JobScrapper") # 앱을 실행함

@app.route("/")	# 사람들이 올 때 route할것. 유저가 방문했을 때 이 함수를 호출한다. 반드시 decorating 되어 있어야 동작한다. 항상 같이 있어야 함.   @는 decorator 이다. 
def home():
    return 'hey there!'


app.run("0.0.0.0")    # Replit에서 하지 않고 로컬에서 해서 좀 다르다..
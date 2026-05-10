from flask import Flask, render_template, request, redirect, send_file
from extractors.wanted import extract_wanted_jobs
from file import save_to_file

app = Flask("JobScrapper") 

db = {}

@app.route("/")	
def home():
    return render_template("home.html", name="nico")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in db:
        wanted_jobs = db[keyword]
    else:
        wanted_jobs = extract_wanted_jobs(keyword)
        db[keyword] = wanted_jobs
    return render_template("search.html", keyword=keyword, wanted_jobs=wanted_jobs)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")   # search 페이지를 거치지 않으면 db에 값이 없음. 다시 keyword를 받아서 서칭할 수 있도록 redirection 시켜준다
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)

app.run("0.0.0.0")    
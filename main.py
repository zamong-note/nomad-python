from flask import Flask, render_template, request
from extractors.wanted import extract_wanted_jobs

app = Flask("JobScrapper") 

db = {}

@app.route("/")	
def home():
    return render_template("home.html", name="nico")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword in db:
        wanted_jobs = db[keyword]
    else:
        wanted_jobs = extract_wanted_jobs(keyword)
        db[keyword] = wanted_jobs
    return render_template("search.html", keyword=keyword, wanted_jobs=wanted_jobs)



app.run("0.0.0.0")    
from flask import Flask, render_template, request
from extractors.wanted import extract_wandted_jobs

app = Flask("JobScrapper") 

@app.route("/")	
def home():
    return render_template("home.html", name="nico")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    wanted = extract_wandted_jobs(keyword)
    return render_template("search.html", keyword=keyword, wanted=wanted)



app.run("0.0.0.0")    
from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)
"""
JOBS = [
  {
    'id':1,
    'title':"Data Analyst",
    "location":"Bengaluru",
    "Salary": "INR 1-5 Lacs"
  },
  {
    'id':2,
    'title':"Cloud Engineer",
    "location":"Delhi",
    "Salary": "INR 4-5 Lacs"
  },
  {
    'id':3,
    'title':"Business Analyst",
    "location":"Mumbai",
    "Salary": "INR 6-10 Lacs"
  }
]
"""

 

@app.route("/")
def hello():
  jobList = load_jobs_from_db()
  return render_template("home.html", jobs=jobList, company_name="Jovian")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(load_jobs_from_db())

@app.route("/job/<id>")
def show_job(id):
  jobIdDetails = load_job_from_db(id)
  if not jobIdDetails:
    return "Not Found", 404
  return render_template("jobpage.html", job=jobIdDetails, company_name = "Jovian")

if __name__ == "__main__":
  app.run(host="0.0.0.0",port="5000", debug=True)

from flask import Flask, render_template, jsonify

app = Flask(__name__)

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

@app.route("/")
def hello():
  return render_template("home.html", jobs=JOBS, company_name="Jovian")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)

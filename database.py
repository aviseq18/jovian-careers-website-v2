from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
from flask import jsonify

dbConnString = os.getenv('DB_CONN_STR')
engine = create_engine(dbConnString)
# mysql://user:password@host/db_name

def configure():
  load_dotenv()

def load_jobs_from_db():
  configure()
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    # print(jobs)
    return jobs 
  
def load_job_from_db(id):
  configure()
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :jobId"),{"jobId":id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()
    
def add_application_to_db(jobId, data):
  configure()
  print("data:", data)
  print("jobId:", jobId)
  print("data[name]:", data["name"])
  with engine.connect() as conn:
    print("aviseq:" , jsonify(data))
    query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) "
                      "VALUES (:jobId, :name, :email, :linkedin, :edu, :work, :resume)")
    conn.execute(query,
              {
                "jobId": jobId,
                "name": data["name"],
                "email": data["email"],
                "linkedin": data["linkedin"],
                "edu": data["edu"],
                "work": data["work"],
                "resume": data["resume"]
              })
    conn.commit()
    conn.close()

# load_jobs_from_db()    
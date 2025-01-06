from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

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

# load_jobs_from_db()    
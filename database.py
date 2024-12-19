from sqlalchemy import create_engine, text

# engine = create_engine("mysql+pymysql://root:ORbjLslmAJFEZDVUCxZbrOXtciJJmXbP@junction.proxy.rlwy.net/joviancareers?host=junction.proxy.rlwy.net?port=18172")
engine = create_engine("mysql+pymysql://root:ORbjLslmAJFEZDVUCxZbrOXtciJJmXbP@junction.proxy.rlwy.net:18172/joviancareers")
# mysql://root:ORbjLslmAJFEZDVUCxZbrOXtciJJmXbP@junction.proxy.rlwy.net:18172/jovian

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://sistema_vendas_dugp_user:GmVnOSCBXs6n85ivGVXezERzuE2rfdp4@dpg-d1ujm415pdvs73fnf2og-a.oregon-postgres.render.com:5432/sistema_vendas_dugp"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """
    Retorna uma sessão de banco de dados.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
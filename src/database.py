from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://sistema_vendas_7zqo_user:74eSCWjIpYgcJ61NHaJ3koMssVB0AGIZ@dpg-d1rdutvdiees73bqunug-a.oregon-postgres.render.com/sistema_vendas_7zqo"

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
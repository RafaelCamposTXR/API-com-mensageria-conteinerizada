from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from logger import logger

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:banco123@10.18.0.20:5432/bd_trabalho_asa"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

if not database_exists(engine.url):
    logger.info("Criando base de dados")
    create_database(engine.url)
else:
    pass

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


logger.info("Iniciando a base de dados")

def get_db():
    db = SessionLocal()
    try:
        logger.info("Base de dados iniciada")
        yield db
    finally:
        db.close()
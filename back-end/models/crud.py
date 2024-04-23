from sqlalchemy.orm import Session
from models import models, schemas


def get_aeroportos(db: Session):
    return db.query(models.Aeroportos).all()

def get_aeroportos_origem(db: Session, cidade: int):
    return db.query(models.Voos).filter(models.Voos.cidade == cidade).all()

def get_voos_data(db: Session, data_saida: int):
    return db.query(models.Voos).filter(models.Voos.data_saida == data_saida).first()

def get_voos_passageiro(db: Session, preco: int, passageiro: int):
    return db.query(models.Voos).filter(models.Voos.passageiros == passageiro).first()








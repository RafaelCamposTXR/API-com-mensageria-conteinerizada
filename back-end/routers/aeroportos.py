from fastapi import FastAPI, APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from schemas import AeroportosSchema
from database.models.aeroporto import Aeroporto
from database import SessionLocal


app = FastAPI()
router = APIRouter()

# conectar com o banco de dados
def obter_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#
# RETORNAR AEROPORTOS
#

@router.get("/aeroportos", response_model=List[AeroportosSchema])
def retornar_aeroportos(db: Session = Depends(obter_db)):
    aeroportos = db.query(Aeroporto).all()
    return aeroportos

#
# RETORNAR AEROPORTOS POR ORIGEM
#

@router.get("/aeroportos/{origem}/destinos", response_model=List[AeroportosSchema])
def retornar_aeroportos_por_origem(origem: str, db: Session = Depends(obter_db)):
    aeroportos_destino = db.query(Aeroporto).filter(Aeroporto.origem == origem).all()
    return aeroportos_destino

#
# CRUD
#

# create
@router.post("/aeroportos/", response_model=AeroportosSchema)
def criar_aeroporto(aeroporto: AeroportosSchema, db: Session = Depends(obter_db)):
    db_aeroporto = Aeroporto(**aeroporto.dict())
    db.add(db_aeroporto)
    db.commit()
    db.refresh(db_aeroporto)
    return db_aeroporto

# get
@router.get("/aeroportos/{aeroporto_id}", response_model=AeroportosSchema)
def obter_aeroporto(aeroporto_id: int, db: Session = Depends(obter_db)):
    db_aeroporto = db.query(Aeroporto).filter(Aeroporto.id == aeroporto_id).first()
    if db_aeroporto is None:
        raise HTTPException(status_code=404, detail="Aeroporto não encontrado")
    return db_aeroporto

# update
@router.put("/aeroportos/{aeroporto_id}", response_model=AeroportosSchema)
def atualizar_aeroporto(aeroporto_id: int, aeroporto: AeroportosSchema, db: Session = Depends(obter_db)):
    db_aeroporto = db.query(Aeroporto).filter(Aeroporto.id == aeroporto_id).first()
    if db_aeroporto is None:
        raise HTTPException(status_code=404, detail="Aeroporto não encontrado")
    for campo, valor in vars(aeroporto).items():
        setattr(db_aeroporto, campo, valor)
    db.commit()
    db.refresh(db_aeroporto)
    return db_aeroporto

# delete
@router.delete("/aeroportos/{aeroporto_id}")
def deletar_aeroporto(aeroporto_id: int, db: Session = Depends(obter_db)):
    db_aeroporto = db.query(Aeroporto).filter(Aeroporto.id == aeroporto_id).first()
    if db_aeroporto is None:
        raise HTTPException(status_code=404, detail="Aeroporto não encontrado")
    db.delete(db_aeroporto)
    db.commit()
    return {"message": "Aeroporto deletado com sucesso"}
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from database.models.voo import Voos
from database.models.database import SessionLocal
from schemas.voos import VoosSchema

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
# RETORNAR VOOS
#

@router.get("/voos/{date}", response_model=list[VoosSchema])
async def retornar_voos(date: str, db: Session = Depends(obter_db)):
    voos = db.query(Voos).filter(Voos.data_saida == date).all()
    return voos

#
# PESQUISAR VOOS
#

@router.get("/voos/search", response_model=List[VoosSchema])
async def pesquisar_voos(origin: int, destination: int, date: str, passengers: int, db: Session = Depends(obter_db)):
    voos = db.query(Voos).filter(Voos.aeroporto_saida == origin, Voos.aeroporto_chegada == destination, Voos.data_saida == date).all()
    search_results = [{"aeroporto_saida": voo.aeroporto_saida, "aeroporto_chegada": voo.aeroporto_chegada, "data_saida": voo.data_saida, "data_chegada": voo.data_chegada, "preco": voo.preco * passengers} for voo in voos]
    return search_results

#
# EFETUAR COMPRA
#

@router.post("/voos/purchase/{id}", response_model=dict)
async def efetuar_compra(id: str, passengers: int, db: Session = Depends(obter_db)):
    voo = db.query(Voos).filter(Voos.id == id).first()
    if not voo:
        raise HTTPException(status_code=404, detail="Voo não encontrado")
    total_price = voo.preco * passengers
    return {"message": "Compra realizada com sucesso", "localizador_reserva": "XYZ123", "numero_etickets": passengers}
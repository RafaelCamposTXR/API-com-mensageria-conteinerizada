from fastapi import FastAPI, APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from datetime import datetime
from pydantic import BaseModel
from database import SessionLocal
from database.models import Voo
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

@router.get("/voos/{date}", response_model=list)
async def retornar_voos(date: str, db: Session = Depends(obter_db)):
    voos = db.query(Voo).filter(Voo.departure_time == date).all()
    flights = [{"flight_number": voo.flight_number, "origin": voo.origin, "destination": voo.destination, "departure_time": voo.departure_time, "arrival_time": voo.arrival_time} for voo in voos]
    return flights

#
# PESQUISAR VOOS
#

@router.get("/voos/search", response_model=list)
async def pesquisar_voos(origin: str, destination: str, date: str, passengers: int, db: Session = Depends(obter_db)):
    voos = db.query(Voo).filter(Voo.origin == origin, Voo.destination == destination, Voo.departure_time == date).all()
    search_results = [{"flight_number": voo.flight_number, "origin": voo.origin, "destination": voo.destination, "departure_time": voo.departure_time, "arrival_time": voo.arrival_time, "price": voo.tarifa * passengers} for voo in voos]
    return search_results

#
# EFETUAR COMPRA
#

@router.post("/voos/purchase/{flight_number}", response_model=dict)
async def efetuar_compra(flight_number: str, passengers: int, db: Session = Depends(obter_db)):
    voo = db.query(Voo).filter(Voo.flight_number == flight_number).first()
    if not voo:
        raise HTTPException(status_code=404, detail="Voo não encontrado")
    total_price = voo.tarifa * passengers
    # Aqui você pode adicionar lógica adicional, como verificar a disponibilidade de assentos, etc.
    return {"message": "Compra realizada com sucesso", "localizador_reserva": "XYZ123", "numero_etickets": passengers}

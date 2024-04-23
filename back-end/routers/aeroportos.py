from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

@router.get("/aeroportos")
async def get_aeroportos():
    # Aqui você implementaria a lógica para obter a lista de aeroportos do seu banco de dados ou de outra fonte de dados
    aeroportos = [
        {"code": "JFK", "name": "John F. Kennedy International Airport", "city": "New York"},
        {"code": "LAX", "name": "Los Angeles International Airport", "city": "Los Angeles"},
        # Adicione mais aeroportos conforme necessário
    ]
    return aeroportos

@router.get("/aeroportos/{origin}")
async def get_aeroportos_by_origin(origin: str):
    # Aqui você implementaria a lógica para obter a lista de aeroportos com base na origem fornecida
    # Por exemplo, filtrar a lista de aeroportos com base na origem
    aeroportos = [
        {"code": "JFK", "name": "John F. Kennedy International Airport", "city": "New York"},
        {"code": "LAX", "name": "Los Angeles International Airport", "city": "Los Angeles"},
        # Adicione mais aeroportos conforme necessário
    ]
    aeroportos_by_origin = [aeroporto for aeroporto in aeroportos if aeroporto["code"] == origin]
    return aeroportos_by_origin
from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

# Rota para obter a lista de todos os aeroportos
@router.get("/voos")
async def get_aeroporto():
    # Parte de Banco de Dados (Felipe)
    return {"aeroportos"}

async def get_aeroportos():
    # Aqui você implementaria a lógica para obter a lista de aeroportos do seu banco de dados ou de outra fonte de dados
    aeroportos = [
        {"code": "JFK", "name": "John F. Kennedy International Airport", "city": "New York"},
        {"code": "LAX", "name": "Los Angeles International Airport", "city": "Los Angeles"},
        # Adicione mais aeroportos conforme necessário
    ]
    return aeroportos

@router.get("/airports/{origin}")
async def get_airports_by_origin(origin: str):
    # Aqui você implementaria a lógica para obter a lista de aeroportos com base na origem fornecida
    # Por exemplo, filtrar a lista de aeroportos com base na origem
    airports = [
        {"code": "JFK", "name": "John F. Kennedy International Airport", "city": "New York"},
        {"code": "LAX", "name": "Los Angeles International Airport", "city": "Los Angeles"},
        # Adicione mais aeroportos conforme necessário
    ]
    airports_by_origin = [airport for airport in airports if airport["code"] == origin]
    return airports_by_origin
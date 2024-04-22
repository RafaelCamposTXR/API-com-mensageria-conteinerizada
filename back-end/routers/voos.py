from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

# Rota para obter a lista de todos os aeroportos
@router.get("/voos")
async def get_aeroporto():
    # Parte de Banco de Dados (Felipe)
    return {"aeroportos"}



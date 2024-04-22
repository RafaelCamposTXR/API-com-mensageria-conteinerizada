from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

@router.get("/aeroportos")
async def get_aeroporto():
    # Parte de Banco de Dados (Felipe)
    return {"aeroportos"}
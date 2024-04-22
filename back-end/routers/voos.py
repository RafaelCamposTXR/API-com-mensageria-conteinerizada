from fastapi import FastAPI

app = FastAPI()

# Rota para obter a lista de todos os aeroportos
@app.get("/lista_aeroportos")
async def get_airports():
    # Parte de Banco de Dados
    return {"aeroportos": aeroportos}

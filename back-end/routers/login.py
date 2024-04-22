# auth.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from models.user import User

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # Aqui você implementaria a lógica para validar o token e obter o usuário associado a ele
    # Por exemplo, verificar no banco de dados se o token é válido e retornar o usuário correspondente
    if token != "fake-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return User(username="user@example.com")

@router.post("/login")
async def login(username: str, password: str):
    # Aqui você implementaria a lógica para autenticar o usuário
    # Por exemplo, verificar no banco de dados se as credenciais são válidas
    return {"access_token": "fake-token", "token_type": "bearer"}

@router.post("/logout")
async def logout():
    # Aqui você implementaria a lógica para invalidar o token de sessão
    # Por exemplo, remover o token do banco de dados ou da lista de tokens válidos
    return {"message": "Logged out successfully"}

@router.get("/validate-session")
async def validate_session(current_user: User = Depends(get_current_user)):
    # Se chegou até aqui, o token é válido e o usuário está autenticado
    return {"message": "Session is valid", "user": current_user}

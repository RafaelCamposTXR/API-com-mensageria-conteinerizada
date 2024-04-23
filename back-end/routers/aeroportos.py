from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import UsuariosSchema
from database.models import Usuarios
from database import SessionLocal
import secrets

app = FastAPI()
router = APIRouter()

# Função para gerar uma chave de sessão única
def generate_session_key():
    return secrets.token_urlsafe(32)

# Função para obter o banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para login
@router.post("/login")
def login_usuario(login_data: UsuariosSchema, db: Session = Depends(get_db)):
    usuario = db.query(Usuarios).filter(Usuarios.email == login_data.email).first()
    if not usuario or usuario.senha != login_data.senha:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Falha no login")
    # Gerar e associar a chave de sessão ao usuário logado
    usuario.chave_sessao = generate_session_key()
    db.commit()
    return {"mensagem": "Login bem-sucedido", "usuario": usuario}

# Endpoint para logout
@router.post("/logout")
def logout(chave_sessao: str, db: Session = Depends(get_db)):
    usuario = db.query(Usuarios).filter(Usuarios.chave_sessao == chave_sessao).first()
    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Chave de sessão inválida")
    # Remover a chave de sessão do usuário
    usuario.chave_sessao = None
    db.commit()
    return {"mensagem": "Logout bem-sucedido"}

# Endpoint para validar sessão
@router.get("/validate-session")
def validate_session(chave_sessao: str, db: Session = Depends(get_db)):
    usuario = db.query(Usuarios).filter(Usuarios.chave_sessao == chave_sessao).first()
    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Chave de sessão inválida")
    return {"mensagem": "Sessão é válida", "usuario": usuario}

app.include_router(router)

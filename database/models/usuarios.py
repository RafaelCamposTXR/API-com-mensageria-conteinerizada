from sqlalchemy import String, Integer, Column, TIMESTAMP, text
from .database import Base, get_db

class Usuarios(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(20), nullable=False)
    senha = Column(String(40), nullable=False)         
    added_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))

# Função para inserir um novo usuário
def inserir_usuario(nome, email, senha):
    session = get_db()
    novo_usuario = Usuarios(nome=nome, email=email, senha=senha)
    session.add(novo_usuario)
    session.commit()
    session.close()

# Função para obter todos os usuários
def obter_usuarios():
    session = get_db()
    usuarios = session.query(Usuarios).all()
    session.close()
    return usuarios

# Função para atualizar um usuário existente
def atualizar_usuario(usuario_id, novo_nome, novo_email, nova_senha):
    session = get_db()
    usuario = session.query(Usuarios).filter_by(id=usuario_id).first()
    if usuario:
        usuario.nome = novo_nome
        usuario.email = novo_email
        usuario.senha = nova_senha
        session.commit()
    session.close()

# Função para deletar um usuário
def deletar_usuario(usuario_id):
    session = get_db()
    usuario = session.query(Usuarios).filter_by(id=usuario_id).first()
    if usuario:
        session.delete(usuario)
        session.commit()
    session.close()
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
def inserir_usuario(usuario_data: UsuarioSchema):
    session = get_db()
    novo_usuario = Usuarios(nome=usuario_data.nome, email=usuario_data.email, senha=usuario_data.senha)
    session.add(novo_usuario)
    session.commit()
    session.close()

# Função para obter todos os usuários
def obter_usuarios() -> List[UsuarioSchema]:
    session = get_db()
    usuarios = session.query(Usuarios).all()
    session.close()
    return [UsuarioSchema(nome=usuario.nome, email=usuario.email, senha=usuario.senha) for usuario in usuarios]

# Função para atualizar um usuário existente
def atualizar_usuario(usuario_id: int, usuario_data: UsuarioSchema):
    session = get_db()
    usuario = session.query(Usuarios).filter_by(id=usuario_id).first()
    if usuario:
        usuario.nome = usuario_data.nome
        usuario.email = usuario_data.email
        usuario.senha = usuario_data.senha
        session.commit()
    session.close()

# Função para deletar um usuário
def deletar_usuario(usuario_id: int):
    session = get_db()
    usuario = session.query(Usuarios).filter_by(id=usuario_id).first()
    if usuario:
        session.delete(usuario)
        session.commit()
    session.close()
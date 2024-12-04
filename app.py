from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import (
    Base, Cerveja, CervejaBase, CervejaIn,
    Pedido, PedidoBase, PedidoIn,
    DetalhesPedidos, DetalhesPedidosBase, DetalhesPedidosIn
)


DATABASE_URL = "sqlite:///./database.sqlite3"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def index():
    return {"Msg": "Bem-vindo ao sistema de gerenciamento de cervejas!"}


@app.post("/cervejas/", response_model=CervejaBase)
def criar_cerveja(cerveja_in: CervejaIn, db: Session = Depends(get_db)):
    """Criar uma nova cerveja."""
    nova_cerveja = Cerveja(**cerveja_in.dict())
    db.add(nova_cerveja)
    db.commit()
    db.refresh(nova_cerveja)
    return nova_cerveja

@app.get("/cervejas/", response_model=list[CervejaBase])
def listar_cervejas(db: Session = Depends(get_db)):
    """Listar todas as cervejas."""
    cervejas = db.query(Cerveja).all()
    return cervejas

@app.get("/cervejas/{cerveja_id}", response_model=CervejaBase)
def obter_cerveja(cerveja_id: int, db: Session = Depends(get_db)):
    """Obter detalhes de uma cerveja específica."""
    cerveja = db.query(Cerveja).filter(Cerveja.id_cerveja == cerveja_id).first()
    if not cerveja:
        raise HTTPException(status_code=404, detail="Cerveja não encontrada")
    return cerveja

@app.put("/cervejas/{cerveja_id}", response_model=CervejaBase)
def atualizar_cerveja(cerveja_id: int, cerveja_in: CervejaIn, db: Session = Depends(get_db)):
    """Atualizar uma cerveja."""
    cerveja = db.query(Cerveja).filter(Cerveja.id_cerveja == cerveja_id).first()
    if not cerveja:
        raise HTTPException(status_code=404, detail="Cerveja não encontrada")
    for key, value in cerveja_in.dict().items():
        setattr(cerveja, key, value)
    db.commit()
    db.refresh(cerveja)
    return cerveja

@app.delete("/cervejas/{cerveja_id}")
def deletar_cerveja(cerveja_id: int, db: Session = Depends(get_db)):
    """Deletar uma cerveja."""
    cerveja = db.query(Cerveja).filter(Cerveja.id_cerveja == cerveja_id).first()
    if not cerveja:
        raise HTTPException(status_code=404, detail="Cerveja não encontrada")
    db.delete(cerveja)
    db.commit()
    return {"Msg": "Cerveja deletada com sucesso"}


@app.post("/pedidos/", response_model=PedidoBase)
def criar_pedido(pedido_in: PedidoIn, db: Session = Depends(get_db)):
    """Criar um novo pedido."""
    novo_pedido = Pedido(**pedido_in.dict())
    db.add(novo_pedido)
    db.commit()
    db.refresh(novo_pedido)
    return novo_pedido

@app.get("/pedidos/", response_model=list[PedidoBase])
def listar_pedidos(db: Session = Depends(get_db)):
    """Listar todos os pedidos."""
    pedidos = db.query(Pedido).all()
    return pedidos

@app.get("/pedidos/{pedido_id}", response_model=PedidoBase)
def obter_pedido(pedido_id: int, db: Session = Depends(get_db)):
    """Obter detalhes de um pedido específico."""
    pedido = db.query(Pedido).filter(Pedido.id_pedido == pedido_id).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido

@app.put("/pedidos/{pedido_id}", response_model=PedidoBase)
def atualizar_pedido(pedido_id: int, pedido_in: PedidoIn, db: Session = Depends(get_db)):
    """Atualizar um pedido."""
    pedido = db.query(Pedido).filter(Pedido.id_pedido == pedido_id).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    for key, value in pedido_in.dict().items():
        setattr(pedido, key, value)
    db.commit()
    db.refresh(pedido)
    return pedido

@app.delete("/pedidos/{pedido_id}")
def deletar_pedido(pedido_id: int, db: Session = Depends(get_db)):
    """Deletar um pedido."""
    pedido = db.query(Pedido).filter(Pedido.id_pedido == pedido_id).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    db.delete(pedido)
    db.commit()
    return {"Msg": "Pedido deletado com sucesso"}


@app.post("/detalhes_pedidos/", response_model=DetalhesPedidosBase)
def criar_detalhes_pedido(detalhes_in: DetalhesPedidosIn, db: Session = Depends(get_db)):
    """Criar detalhes de um pedido."""
    novo_detalhe = DetalhesPedidos(**detalhes_in.dict())
    db.add(novo_detalhe)
    db.commit()
    db.refresh(novo_detalhe)
    return novo_detalhe

@app.get("/detalhes_pedidos/", response_model=list[DetalhesPedidosBase])
def listar_detalhes_pedidos(db: Session = Depends(get_db)):
    """Listar todos os detalhes dos pedidos."""
    detalhes = db.query(DetalhesPedidos).all()
    return detalhes

@app.put("/detalhes_pedidos/{pedido_id}/{cerveja_id}", response_model=DetalhesPedidosBase)
def atualizar_detalhes_pedido(
    pedido_id: int,
    cerveja_id: int,
    detalhes_in: DetalhesPedidosIn,
    db: Session = Depends(get_db),
):
    """Atualizar detalhes de um pedido."""
    detalhe = db.query(DetalhesPedidos).filter(
        DetalhesPedidos.id_pedido == pedido_id,
        DetalhesPedidos.id_cerveja == cerveja_id,
    ).first()
    if not detalhe:
        raise HTTPException(status_code=404, detail="Detalhes do pedido não encontrados")
    for key, value in detalhes_in.dict().items():
        setattr(detalhe, key, value)
    db.commit()
    db.refresh(detalhe)
    return detalhe

@app.delete("/detalhes_pedidos/{pedido_id}/{cerveja_id}")
def deletar_detalhes_pedido(pedido_id: int, cerveja_id: int, db: Session = Depends(get_db)):
    """Deletar detalhes de um pedido."""
    detalhe = db.query(DetalhesPedidos).filter(
        DetalhesPedidos.id_pedido == pedido_id,
        DetalhesPedidos.id_cerveja == cerveja_id,
    ).first()
    if not detalhe:
        raise HTTPException(status_code=404, detail="Detalhes do pedido não encontrados")
    db.delete(detalhe)
    db.commit()
    return {"Msg": "Detalhes do pedido deletados com sucesso"}

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Cerveja, CervejaBase, CervejaIn

DATABASE_URL = "sqlite:///./database.sqlite3"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permitir o front-end React
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)



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

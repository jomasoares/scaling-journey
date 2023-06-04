from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/corretores/")
def create_corretor(corretor: schemas.Corretor, db: Session = Depends(get_db)):
    db_corretor = crud.get_corretor(db, corretor_id=corretor.corretorId)
    if db_corretor:
        raise HTTPException(status_code=400, detail="corretor ja existe")
    db_corretor = models.Corretor(
        corretorId=corretor.corretorId,
        cpfCnpj=corretor.cpfCnpj,
        protocolo=corretor.protocolo,
        nome=corretor.nome,
        recadastrado=corretor.recadastrado,
        situacao=corretor.situacao,
        produtos=corretor.produtos)
    return crud.create_corretor(db=db, corretor=db_corretor)

@app.get("/corretores/{corretor_id}")
def get_corretor(corretor_id: str, db: Session = Depends(get_db)):
    db_user = crud.get_corretor(db, corretor_id=corretor_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user



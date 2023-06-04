from sqlalchemy.orm import Session
from . import models

def get_corretor(db: Session, corretor_id: int):
    return db.query(models.Corretor).filter(models.Corretor.corretorId == corretor_id).first()

def create_corretor(db: Session, corretor: models.Corretor):
    db.add(corretor)
    db.commit()
    return corretor


#CRUD básico
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_session
from models import Target
from pydantic import BaseModel, HttpUrl
from typing import List

router = APIRouter() # Agrupar rotas da API

class TargetCreate(BaseModel): # modelo de entrada em base da url
    url: HttpUrl

class TargetResponse(BaseModel): # modelo de saida para a resposta da API
    id: int
    url: str
    enabled: bool

    class Config:
        orm_mode = True

@router.post("/targets", response_model=TargetResponse) # Cria um novo target (POST)
# /TARGETS, /TARGETS/{id} endpoits REST via HTTP
def create_target(target: TargetCreate, db: Session = Depends(get_session)): # depends - injeta a sessão do banco com SQLAlchemy
    new_target = Target(url=target.url)
    db.add(new_target)
    db.commit()
    db.refresh(new_target)
    return new_target

@router.get("/targets", response_model=List[TargetResponse])
def list_targets(db: Session = Depends(get_session)):
    return db.query(Target).all()

@router.get("/targets/{target_id}", response_model=TargetResponse)
def get_target(target_id: int, db: Session = Depends(get_session)):
    target = db.query(Target).get(target_id)
    if not target:
        raise HTTPException(status_code=404, detail="Target not found")
    return target

@router.delete("/targets/{target_id}")
def delete_target(target_id: int, db: Session = Depends(get_session)):
    target = db.query(Target).get(target_id)
    if not target:
        raise HTTPException(status_code=404, detail="Target not found")
    db.delete(target)
    db.commit()
    return {"ok": True}

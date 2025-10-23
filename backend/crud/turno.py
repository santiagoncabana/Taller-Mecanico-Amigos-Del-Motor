from fastapi import APIRouter, Depends, HTTPException
from ..database.database import get_db, Session

router = APIRouter()

#turnos endpoints

# @router.post("/turnos", tags=["turnos"])
# def create_turno():

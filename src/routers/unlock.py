from fastapi import APIRouter, Depends
from src.utils.abbr import to_abbr
from fastapi import FastAPI, Depends
from fastapi import APIRouter, HTTPException, Form
from sqlalchemy.orm import Session
from src.database.connect import get_db
from src.database.models import Letter
from typing import List, Dict, Annotated
from pydantic import BaseModel
router = APIRouter()

class unlock_letter_Request(BaseModel):
    id: int
    pin: str

@router.post("/")
async def unlock_letter(req : unlock_letter_Request, db: Session = Depends(get_db)):
    # Mock function to simulate database search
    # In a real application, this would query the database
    letter = db.query(Letter).filter(Letter.id == req.id).first()
    if letter:
        if letter.pin == req.pin:
            return {"message": "Letter unlocked successfully", "letter": letter}
        else:
            return {"error": "Incorrect pin"}
    else:
        return {"error": "Letter not found"}
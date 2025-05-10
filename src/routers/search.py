from fastapi import APIRouter, Depends
from src.utils.abbr import to_abbr
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.database.connect import get_db
from src.database.models import Letter
router = APIRouter()

def find_letter_by_abbr(abbr: str, db):
    # Mock function to simulate database search
    # In a real application, this would query the database
    return db.filter(Letter.abbr_receiver == abbr)

def find_letter_by_group(group: int, db):
    # Mock function to simulate database search
    # In a real application, this would query the database
    return db.filter(Letter.group_receiver_id == group)
    
@router.get("/{name}")
async def search_items(name: str, db: Session = Depends(get_db)):
    abbr_name = to_abbr(name)
    # Filter mock data by receiver's abbreviation
    results = find_letter_by_abbr(abbr_name, db.query(Letter)).all()
    return {"letters": results}


@router.get("/{name}/{group}")
async def search_items_w_group(name: str, group: int, db: Session = Depends(get_db)):
    abbr_name = to_abbr(name)
    # Filter mock data by receiver's abbreviation and group (mock logic for group)
    results = find_letter_by_group(group, find_letter_by_abbr(abbr_name, db.query(Letter))).all()
    return {"letters": results}
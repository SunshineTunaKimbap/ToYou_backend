from fastapi import APIRouter
from src.utils.abbr import to_abbr
from src.database.connect import get_db
from src.database.models import Letter
router = APIRouter()

def find_letter_by_abbr(abbr: str, db):
    # Mock function to simulate database search
    # In a real application, this would query the database
    return db.query(Letter).filter(Letter.abbr_receiver == abbr).all()
    

@router.get("/{name}")
async def search_items(name: str):
    abbr_name = to_abbr(name)
    # Filter mock data by receiver's abbreviation
    results = find_letter_by_abbr(abbr_name)
    return {"letters": results}

@router.get("/{name}/{group}")
async def search_items(name: str, group: str):
    # Filter mock data by receiver's abbreviation and group (mock logic for group)
    results = [letter for letter in mock_data if letter["abbr_receiver"] == name]
    return {"letters": results}
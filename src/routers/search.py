from fastapi import APIRouter, Depends
from src.utils.abbr import to_abbr
from src.database.connect import get_db
from src.database.models import Letter
router = APIRouter()

mock_data = [
    {"id": 1, "content": "Hello, this is a test letter.", "abbr_receiver": "ㄱㄷ"},
    {"id": 2, "content": "Another letter for testing.", "abbr_receiver": "ㄱㄷ"},
]

async def search_items(name: str):
    abbr_name = to_abbr(name)
    # Filter mock data by receiver's abbreviation
    results = [letter for letter in mock_data if letter["abbr_receiver"] == abbr_name]
    return {"letters": results}


@router.get("/{name}/{group}")
async def search_items(name: str, group: str):
    # Filter mock data by receiver's abbreviation and group (mock logic for group)
    results = [letter for letter in mock_data if letter["abbr_receiver"] == name]
    return {"letters": results}
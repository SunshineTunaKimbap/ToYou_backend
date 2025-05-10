from fastapi import APIRouter, HTTPException
from typing import List, Dict

router = APIRouter()

@router.get("/")
async def get_letter(letter_id="1") -> Dict[str, str]:
    """
    Get a letter by its ID.
    """
    # Simulate fetching a letter from a database
    if letter_id == "1":
        return {"id": "1", "content": "Hello, this is a test letter."}
    else:
        raise HTTPException(status_code=404, detail="Letter not found")
from fastapi import APIRouter, Depends
from src.utils.abbr import to_abbr
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.database.connect import get_db
from src.database.models import Letter, ReceiverGroup
router = APIRouter()

def find_letter_by_abbr(abbr: str, db):
    # Mock function to simulate database search
    # In a real application, this would query the database
    return db.filter(Letter.abbr_receiver == abbr)

def find_letter_by_group(group: int, db):
    # Mock function to simulate database search
    # In a real application, this would query the database
    return db.filter(Letter.group_receiver_id == group)
    
def letter_to_dict(letters, db):
    return [
        {
            "id": r[0],
            "abbr_sender": r[1],
            "abbr_receiver": r[2],
            "content": r[3],
            "group_receiver_id": r[4],
            "group_receiver": (
                db.query(ReceiverGroup).filter(ReceiverGroup.id == r[4]).first()
            ).name if db.query(ReceiverGroup).filter(ReceiverGroup.id == r[4]).first() else "Unknown Group",
            "locked": (r[5] is not None)
        }
        for r in letters.with_entities(Letter.id, Letter.abbr_sender, Letter.abbr_receiver, Letter.content, Letter.group_receiver_id, Letter.pin)
        .all()
        ]
@router.get("/{name}")
async def search_items(name: str, db: Session = Depends(get_db)):
    abbr_name = to_abbr(name)
    # Query specific fields
    results = (
        find_letter_by_abbr(abbr_name, db.query(Letter))
    )
    # Convert results to a list of dictionaries
    letters = letter_to_dict(results, db)
    return {"letters": letters}


@router.get("/{name}/{group}")
async def search_items_w_group(name: str, group: int, db: Session = Depends(get_db)):
    abbr_name = to_abbr(name)
    results = (
        find_letter_by_group(group, find_letter_by_abbr(abbr_name, db.query(Letter)))
    )
    letters = letter_to_dict(results, db)
    return {"letters": letters}
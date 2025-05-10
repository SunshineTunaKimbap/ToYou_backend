from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, Form
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List, Dict, Annotated
from src.utils.abbr import to_abbr
from src.database.connect import get_db
from src.database.models import Letter

router = APIRouter()

class Letter_Request(BaseModel):
    name_sender: str
    name_receiver: str
    content: str
    group_receiver_id: int | None = 0
    design_id: int | None = 0
    pin: str | None = None
    content_secret: str | None = None

@router.post("/")
async def create_letter(post: Letter_Request, db: Session = Depends(get_db)):
    """
    Create a new post.
    """
    # Simulate saving the post to a database
    # In a real application, you would save the post to a database here
    new_post = Letter(
        name_sender=post.name_sender,
        abbr_sender=to_abbr(post.name_sender),
        name_receiver=post.name_receiver,
        abbr_receiver=to_abbr(post.name_receiver),
        content=post.content,
        group_receiver_id=post.group_receiver_id,
        design_id=post.design_id,
        content_secret=post.content_secret,
        pin=post.pin
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"message": "Post created successfully", "post": new_post}
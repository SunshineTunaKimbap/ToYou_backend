from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, Form
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List, Dict, Annotated
from src.utils.abbr import to_abbr
from src.database.connect import get_db
from src.database.models import Letter

router = APIRouter()

def confirm_content(content: str) -> dict:
    if len(content) == 0:
        return {"error": "Content cannot be empty"}
    if len(content) > 50:
        return {"error": "Content is too long"}
    return {"success": "Content is valid"}
    

class Letter_Request(BaseModel):
    name_sender: str
    name_receiver: str
    content: str
    group_receiver_id: int | None = 0
    design_id: int | None = 0
    pin: str | None = None
    content_secret: str | None = None
from fastapi import HTTPException, status

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_letter(post: Letter_Request, db: Session = Depends(get_db)):
    """
    Create a new post.
    """
    # Validate content
    validation_result = confirm_content(post.content)
    if "error" in validation_result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=validation_result["error"]
        )

    try:
        # Check if the sender and receiver names are valid
        abbr_sender = to_abbr(post.name_sender)
        abbr_receiver = to_abbr(post.name_receiver)
        if not abbr_sender or not abbr_receiver:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid sender or receiver name"
            )
        if not (7 > len(abbr_sender) > 1) or not (7 > len(abbr_receiver) > 1):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Abbreviations must be 2~6 characters long"
            )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error generating abbreviation: {str(e)}"
        )
    
    # Create a new Letter object
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

    # Save to the database
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    # Return success response with HTTP 201 status
    return {"message": "Post created successfully", "post": new_post}
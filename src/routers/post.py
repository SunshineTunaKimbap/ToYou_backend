from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, Form
from typing import List, Dict, Annotated
from src.utils.abbr import to_abbr

router = APIRouter()

class Letter_Request(BaseModel):
    name_sender: str
    name_receiver: str
    content: str
class Letter(BaseModel):
    name_sender : str
    abbr_sender : str
    name_receiver : str
    abbr_receiver : str
    content : str

@router.post("/")
async def create_post(post: Letter_Request):
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
        content=post.content
    )
    return {"message": "Post created successfully", "post": new_post}
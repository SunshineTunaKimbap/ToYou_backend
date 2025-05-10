from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.routers import search, post
from src.database.connect import get_db
from src.database.models import Letter


app = FastAPI()

app.include_router(search.router, prefix="/api/search", tags=["Search"])
app.include_router(post.router, prefix="/api/post", tags=["Post"])

@app.get("/")
async def root():
    return {"message": "ㄱㄷ에게!"}


@app.get("/")
async def search_items(db: Session = Depends(get_db)):
    return db.query(Letter).all()
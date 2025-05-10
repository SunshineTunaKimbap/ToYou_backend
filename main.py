from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.routers import search, post, unlock
from src.database.connect import DB_props, get_db
from src.database.models import Letter

DB = DB_props.get_instance()
app = FastAPI()

app.include_router(search.router, prefix="/api/search", tags=["Search"])
app.include_router(post.router, prefix="/api/post", tags=["Post"])
app.include_router(unlock.router, prefix="/api/unlock", tags=["Unlock"])

@app.get("/")
async def root(db: Session = Depends(get_db)):
    return db.query(Letter).all()
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.routers import search, post, unlock
from src.database.connect import DB_props, get_db
from src.database.models import Letter
from fastapi.middleware.cors import CORSMiddleware


DB = DB_props.get_instance()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 개발 시 전체 허용, 배포 시엔 도메인 제한
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(search.router, prefix="/api/search", tags=["Search"])
app.include_router(post.router, prefix="/api/post", tags=["Post"])
app.include_router(unlock.router, prefix="/api/unlock", tags=["Unlock"])

@app.get("/")
async def root(db: Session = Depends(get_db)):
    return db.query(Letter).all()
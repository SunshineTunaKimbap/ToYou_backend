from fastapi import FastAPI
from src.routers import search, post

app = FastAPI()

app.include_router(search.router, prefix="/api/search", tags=["Search"])
app.include_router(post.router, prefix="/api/post", tags=["Post"])

@app.get("/")
async def root():
    return {"message": "ㄱㄷ에게!"}
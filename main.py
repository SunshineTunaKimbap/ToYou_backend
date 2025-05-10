from fastapi import FastAPI
from src.routers import letter, search

app = FastAPI()

app.include_router(letter.router, prefix="/api/letter", tags=["Letter"])
app.include_router(search.router, prefix="/api/search", tags=["Search"])

@app.get("/")
async def root():
    return {"message": "ㄱㄷ에게!"}
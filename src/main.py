from fastapi import FastAPI
from routers import letter, search

app = FastAPI()

app.include_router(letter.router, prefix="/api/letter", tags=["Letter"])
app.include_router(search.router, prefix="/api/search", tags=["Search"])
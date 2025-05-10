from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "SUNSHINE TUNA KIMBAP SKYST"
    }

@app.get("/favicon.ico")
async def favicon():
    return {}



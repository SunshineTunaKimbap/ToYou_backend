from fastapi import APIRouter

router = APIRouter()

@router.get("/{name}")
async def search_items(name: str):
    # look up the name in the database
    # and return the results
    return {"letters": [
        {"id": 1, "content": "Hello, this is a test letter."},
        {"id": 2, "content": "This is another test letter."}
    ]}

@router.get("/{name}/{group}")
async def search_items(name: str, group: str):
    return {"letters": [
        {"id": 1, "content": f"Hello, this is a test letter to {name} in {group}."},
        {"id": 2, "content": "This is another test letter."}
    ]}
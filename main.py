from typing import Annotated
from fastapi import Depends, FastAPI

app = FastAPI()

async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 10):
    return {"q": q, "skip": skip, "limit": limit}

CommonsDep = Annotated[dict, Depends(common_parameters)]

fake_elements_db = [
    {"id": 1, "name": "Hidrogênio", "symbol": "H", "atomic_number": 1},
    {"id": 2, "name": "Hélio", "symbol": "He", "atomic_number": 2},
    {"id": 3, "name": "Lítio", "symbol": "Li", "atomic_number": 3},
    {"id": 4, "name": "Berílio", "symbol": "Be", "atomic_number": 4},
    {"id": 5, "name": "Boro", "symbol": "B", "atomic_number": 5},
]

@app.get("/elements/")
async def list_elements(commons: CommonsDep):
    elements = [
        elem for elem in fake_elements_db
        if commons["q"].lower() in elem["name"].lower() or commons["q"].lower() in elem["symbol"].lower()
    ] if commons["q"] else fake_elements_db

    return elements[commons["skip"]:commons["skip"] + commons["limit"]]

@app.get("/elements/{element_id}")
async def get_element(element_id: int, commons: CommonsDep):
    element = next((elem for elem in fake_elements_db if elem["id"] == element_id), None)
    
    if element is None:
        return {"error": "Elemento não encontrado"}

    return {"element": element, "filters": commons}

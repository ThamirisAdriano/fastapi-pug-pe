from fastapi import  FastAPI

app = FastAPI()

elements_db = [
    {"id": 1, "name": "Hidrogênio", "symbol": "H", "atomic_number": 1},
    {"id": 2, "name": "Hélio", "symbol": "He", "atomic_number": 2},
    {"id": 3, "name": "Lítio", "symbol": "Li", "atomic_number": 3},
    {"id": 4, "name": "Berílio", "symbol": "Be", "atomic_number": 4},
    {"id": 5, "name": "Boro", "symbol": "B", "atomic_number": 5},
]

@app.get("/")
def home():
    return (elements_db)

@app.get("/elements/sum")
def atomic_number_sum():
    return {"sum": sum(e["atomic_number"] for e in elements_db)}

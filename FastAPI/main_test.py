from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TestModel(BaseModel):
    name: str
    age: int

@app.post("/test")
def test_endpoint(data: TestModel):
    return {"message": f"{data.name} a {data.age} ans"}


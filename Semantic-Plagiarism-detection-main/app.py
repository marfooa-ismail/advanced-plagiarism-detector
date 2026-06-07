from fastapi import FastAPI
from pydantic import BaseModel
from inference import check_plagiarism

app = FastAPI(title="Plagiarism Detection API")

class TextInput(BaseModel):
    text1: str
    text2: str

@app.post("/check")
def check_endpoint(data: TextInput):
    return check_plagiarism(data.text1, data.text2)

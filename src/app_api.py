# src/app_api.py

from fastapi import FastAPI
from pydantic import BaseModel
from src.prompt_builder import build_prompt
from src.model_client import query_openai

app = FastAPI()

class RequestBody(BaseModel):
    task: str
    input_text: str
    model: str

@app.post("/run_task/")
async def run_task(body: RequestBody):
    prompt = build_prompt(body.task, body.input_text)
    result = query_openai(prompt, model=body.model)
    return {"result": result}


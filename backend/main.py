from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data import QUESTIONS
from mbti_logic import calculate_result

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/questions")
def get_questions():
    return QUESTIONS

@app.post("/result")
def get_result(payload: dict):
    answers = payload.get("answers", [])
    return calculate_result(answers)

@app.get("/health")
def health():
    return {"status": "ok"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from data import QUESTIONS
from mbti_logic import calculate_result

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 👉 프론트 정적 서빙
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

@app.get("/questions")
def get_questions():
    return QUESTIONS

@app.post("/result")
def get_result(payload: dict):
    answers = payload.get("answers", [])
    return calculate_result(answers)

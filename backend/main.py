from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from data import QUESTIONS
from mbti_logic import calculate_result

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>점심 MBTI 테스트</title>
</head>
<body>
  <h1>🍱 점심 MBTI 테스트</h1>
  <div id="app"></div>

  <script>
    let answers = [];
    let idx = 0;

    fetch("/questions")
      .then(r => r.json())
      .then(qs => {
        window.qs = qs;
        render();
      });

    function render() {
      if (idx >= qs.length) {
        fetch("/result", {
          method: "POST",
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({ answers })
        })
        .then(r => r.json())
        .then(res => {
          document.getElementById("app").innerHTML =
            "<h2>당신의 점심 MBTI는 " + res.mbti + "</h2><p>" + res.menu + "</p>";
        });
        return;
      }

      const q = qs[idx];
      document.getElementById("app").innerHTML = `
        <p>${q.question}</p>
        <button onclick="choose(0)">${q.options[0].text}</button>
        <button onclick="choose(1)">${q.options[1].text}</button>
      `;
    }

    function choose(v) {
      answers.push(v);
      idx++;
      render();
    }
  </script>
</body>
</html>
"""

const API = "";

let questions = [];
let answers = [];
let index = 0;

async function loadQuestions() {
  const res = await fetch(`${API}/questions`);
  questions = await res.json();
  render();
}

function render() {
  const app = document.getElementById("app");
  app.innerHTML = "";

  if (index >= questions.length) {
    submit();
    return;
  }

  const q = questions[index];
  app.innerHTML += `<h3>${q.question}</h3>`;

  Object.entries(q.options).forEach(([key, value]) => {
    const btn = document.createElement("button");
    btn.innerText = value;
    btn.onclick = () => {
      answers.push(key);
      index++;
      render();
    };
    app.appendChild(btn);
  });
}

async function submit() {
  const res = await fetch(`${API}/result`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ answers })
  });

  const data = await res.json();
  document.getElementById("app").innerHTML = `
    <h2>${data.type}</h2>
    <h3>오늘의 점심: 🍽️ ${data.menu}</h3>
    <p>MBTI 코드: ${data.mbti}</p>
  `;
}

loadQuestions();

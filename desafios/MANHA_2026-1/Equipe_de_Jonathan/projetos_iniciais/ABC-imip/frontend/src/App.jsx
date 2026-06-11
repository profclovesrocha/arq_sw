import { useEffect, useState } from "react";
import "./App.css";

function App() {

  const [questions, setQuestions] = useState([]);
  const [current, setCurrent] = useState(0);
  const [answer, setAnswer] = useState("");
  const [answers, setAnswers] = useState([]);

  // Guarda o resultado vindo do backend
  const [result, setResult] = useState(null);

  useEffect(() => {

    fetch("http://localhost:5000/quizzes/1")
      .then(res => res.json())
      .then(data => {
        setQuestions(data.questions);
      });

  }, []);

  async function submitQuiz(finalAnswers) {

  const response = await fetch(
    "http://localhost:5000/quizzes/submit",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        quiz_id: 1,
        answers: finalAnswers
      })
    }
  );

  const data = await response.json();

  console.log(data);

  setResult(data);

  return data; // importante
}

  async function nextQuestion() {

  if (!answer.trim()) {
    alert("Digite uma resposta!");
    return;
  }

  const updatedAnswers = [
    ...answers,
    {
      question_id: questions[current].id,
      student_answer: answer
    }
  ];

  setAnswers(updatedAnswers);

  setAnswer("");

  
  if (current < questions.length - 1) {
    setCurrent(current + 1);
    return;
  }

 
  await submitQuiz(updatedAnswers);
  setCurrent(current + 1); 
}

  if (questions.length === 0) {
    return <h1>Carregando...</h1>;
  }

  if (current >= questions.length) {

    return (
      <div className="quiz-container">

        <h1>🎉 Parabéns!!! 🎉</h1>

        <h2>Você terminou o quiz!</h2>

        {result && (
          <>
            <h3>
              Você acertou {result.correct_answers} de {result.total_questions} questões!
            </h3>

            <p>
              Erros: {result.wrong_answers}
            </p>
          </>
        )}

      </div>
    );
  }

  return (
    <div className="quiz-container">

      <h1 className="quiz-title">
        🌟 Quiz das Vogais 🌟
      </h1>

      <p className="progress">
        Pergunta {current + 1} de {questions.length}
      </p>

      <p>Complete a palavra:</p>

      <h2 className="question">
        {questions[current].word_with_missing}
      </h2>

      <input
        className="answer-input"
        type="text"
        value={answer}
        onChange={(e) =>
          setAnswer(e.target.value.toUpperCase())
        }
        maxLength="1"
        placeholder="?"
      />

      <br />
      <br />

      <button
        className="next-button"
        onClick={nextQuestion}
      >
        Próxima ➡️
      </button>

    </div>
  );
}

export default App;
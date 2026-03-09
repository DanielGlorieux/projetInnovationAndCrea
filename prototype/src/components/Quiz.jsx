import { useState, useEffect, useCallback } from "react";
import quizData from "../data/quizData";
import "./Quiz.css";

const TOTAL_TIME_SECONDS = 45 * 60; // 45 minutes

function formatTime(seconds) {
  const m = Math.floor(seconds / 60);
  const s = seconds % 60;
  return `${m.toString().padStart(2, "0")}:${s.toString().padStart(2, "0")}`;
}

function shuffleArray(array) {
  const shuffled = [...array];
  for (let i = shuffled.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
  }
  return shuffled;
}

export default function Quiz() {
  const [started, setStarted] = useState(false);
  const [finished, setFinished] = useState(false);
  const [currentQ, setCurrentQ] = useState(0);
  const [answers, setAnswers] = useState({});
  const [showExplanation, setShowExplanation] = useState(false);
  const [timeLeft, setTimeLeft] = useState(TOTAL_TIME_SECONDS);
  const [questions] = useState(() => shuffleArray(quizData));

  const finishQuiz = useCallback(() => {
    setFinished(true);
    setStarted(false);
  }, []);

  // Timer
  useEffect(() => {
    if (!started || finished) return;
    if (timeLeft <= 0) {
      finishQuiz();
      return;
    }
    const timer = setInterval(() => {
      setTimeLeft((t) => t - 1);
    }, 1000);
    return () => clearInterval(timer);
  }, [started, finished, timeLeft, finishQuiz]);

  const handleAnswer = (questionId, optionIndex) => {
    if (answers[questionId] !== undefined) return; // already answered
    setAnswers((prev) => ({ ...prev, [questionId]: optionIndex }));
    setShowExplanation(true);
  };

  const nextQuestion = () => {
    setShowExplanation(false);
    if (currentQ < questions.length - 1) {
      setCurrentQ((q) => q + 1);
    } else {
      finishQuiz();
    }
  };

  const prevQuestion = () => {
    setShowExplanation(false);
    if (currentQ > 0) {
      setCurrentQ((q) => q - 1);
    }
  };

  const score = questions.reduce((acc, q) => {
    return acc + (answers[q.id] === q.correct ? 1 : 0);
  }, 0);

  const answeredCount = Object.keys(answers).length;

  // ===== START SCREEN =====
  if (!started && !finished) {
    return (
      <div className="quiz-container">
        <div className="quiz-start">
          <div className="quiz-start-icon">📝</div>
          <h1>QCM — Challenge Innovation</h1>
          <p className="quiz-subtitle">
            Cours : &laquo; De la théorie à la valeur par l&apos;innovation
            &raquo;
          </p>

          <div className="quiz-info-grid">
            <div className="quiz-info-card">
              <span className="info-number">30</span>
              <span className="info-label">Questions</span>
            </div>
            <div className="quiz-info-card">
              <span className="info-number">45</span>
              <span className="info-label">Minutes</span>
            </div>
            <div className="quiz-info-card">
              <span className="info-number">3</span>
              <span className="info-label">Modules</span>
            </div>
          </div>

          <div className="quiz-modules-preview">
            <h3>Modules couverts :</h3>
            <ul>
              <li>
                <strong>Module I</strong> — Introduction au Challenge Innovation
                (10 questions)
              </li>
              <li>
                <strong>Module II</strong> — Méthodologies d&apos;Innovation :
                Design Thinking &amp; Problem-Driven (12 questions)
              </li>
              <li>
                <strong>Module III</strong> — Préparation et Pitch du Projet (8
                questions)
              </li>
            </ul>
          </div>

          <div className="quiz-rules">
            <h3>⚠️ Règles :</h3>
            <ul>
              <li>Les questions sont mélangées aléatoirement</li>
              <li>Une seule bonne réponse par question</li>
              <li>
                Chaque réponse est définitive — vous ne pouvez pas la changer
              </li>
              <li>L&apos;explication s&apos;affiche après chaque réponse</li>
              <li>Le temps est limité à 45 minutes</li>
            </ul>
          </div>

          <button className="quiz-btn quiz-btn-start" onClick={() => setStarted(true)}>
            🚀 Commencer le QCM
          </button>
        </div>
      </div>
    );
  }

  // ===== RESULTS SCREEN =====
  if (finished) {
    const percentage = Math.round((score / questions.length) * 100);
    let grade, gradeClass;
    if (percentage >= 90) {
      grade = "Excellent ! 🏆";
      gradeClass = "grade-excellent";
    } else if (percentage >= 75) {
      grade = "Très bien ! 🎉";
      gradeClass = "grade-good";
    } else if (percentage >= 60) {
      grade = "Bien 👍";
      gradeClass = "grade-ok";
    } else if (percentage >= 50) {
      grade = "Passable ⚠️";
      gradeClass = "grade-pass";
    } else {
      grade = "À retravailler 📚";
      gradeClass = "grade-fail";
    }

    // Group by module
    const moduleGroups = {};
    questions.forEach((q) => {
      if (!moduleGroups[q.module]) moduleGroups[q.module] = [];
      moduleGroups[q.module].push(q);
    });

    return (
      <div className="quiz-container">
        <div className="quiz-results">
          <h1>Résultats du QCM</h1>

          <div className={`quiz-score-display ${gradeClass}`}>
            <div className="score-circle">
              <span className="score-number">{score}</span>
              <span className="score-total">/{questions.length}</span>
            </div>
            <div className="score-details">
              <span className="score-percentage">{percentage}%</span>
              <span className="score-grade">{grade}</span>
            </div>
          </div>

          <div className="quiz-stats-bar">
            <div className="stat-item correct-stat">
              ✅ Correctes : {score}
            </div>
            <div className="stat-item wrong-stat">
              ❌ Incorrectes : {answeredCount - score}
            </div>
            <div className="stat-item skip-stat">
              ⏭️ Non répondues : {questions.length - answeredCount}
            </div>
          </div>

          {/* Module breakdown */}
          <div className="module-breakdown">
            <h2>Détail par module</h2>
            {Object.entries(moduleGroups).map(([module, qs]) => {
              const moduleScore = qs.reduce(
                (a, q) => a + (answers[q.id] === q.correct ? 1 : 0),
                0
              );
              const modulePercent = Math.round(
                (moduleScore / qs.length) * 100
              );
              return (
                <div key={module} className="module-score-row">
                  <span className="module-name">{module}</span>
                  <div className="module-bar">
                    <div
                      className="module-bar-fill"
                      style={{
                        width: `${modulePercent}%`,
                        background:
                          modulePercent >= 70
                            ? "#43a047"
                            : modulePercent >= 50
                            ? "#f9a825"
                            : "#e53935",
                      }}
                    />
                  </div>
                  <span className="module-percent">
                    {moduleScore}/{qs.length} ({modulePercent}%)
                  </span>
                </div>
              );
            })}
          </div>

          {/* Review all questions */}
          <div className="quiz-review">
            <h2>📋 Revue complète des questions</h2>
            {questions.map((q, idx) => {
              const userAnswer = answers[q.id];
              const isCorrect = userAnswer === q.correct;
              const wasAnswered = userAnswer !== undefined;
              return (
                <div
                  key={q.id}
                  className={`review-item ${
                    wasAnswered
                      ? isCorrect
                        ? "review-correct"
                        : "review-wrong"
                      : "review-skipped"
                  }`}
                >
                  <div className="review-header">
                    <span className="review-number">Q{idx + 1}</span>
                    <span className="review-module-tag">{q.module}</span>
                    <span className="review-status">
                      {wasAnswered
                        ? isCorrect
                          ? "✅"
                          : "❌"
                        : "⏭️"}
                    </span>
                  </div>
                  <p className="review-question">{q.question}</p>
                  <div className="review-options">
                    {q.options.map((opt, i) => (
                      <div
                        key={i}
                        className={`review-option ${
                          i === q.correct ? "option-correct" : ""
                        } ${
                          i === userAnswer && i !== q.correct
                            ? "option-wrong"
                            : ""
                        }`}
                      >
                        <span className="option-letter">
                          {String.fromCharCode(65 + i)}
                        </span>
                        {opt}
                      </div>
                    ))}
                  </div>
                  <div className="review-explanation">
                    <strong>💡 Explication :</strong> {q.explanation}
                  </div>
                </div>
              );
            })}
          </div>

          <button
            className="quiz-btn quiz-btn-start"
            onClick={() => {
              setFinished(false);
              setCurrentQ(0);
              setAnswers({});
              setShowExplanation(false);
              setTimeLeft(TOTAL_TIME_SECONDS);
            }}
          >
            🔄 Recommencer le QCM
          </button>
        </div>
      </div>
    );
  }

  // ===== QUESTION SCREEN =====
  const q = questions[currentQ];
  const userAnswer = answers[q.id];
  const hasAnswered = userAnswer !== undefined;

  return (
    <div className="quiz-container">
      {/* Top bar */}
      <div className="quiz-topbar">
        <div className="quiz-progress-info">
          <span>
            Question {currentQ + 1}/{questions.length}
          </span>
          <span className="quiz-answered">
            {answeredCount} répondue{answeredCount !== 1 ? "s" : ""}
          </span>
        </div>
        <div
          className={`quiz-timer ${timeLeft < 300 ? "timer-warning" : ""} ${
            timeLeft < 60 ? "timer-critical" : ""
          }`}
        >
          ⏱️ {formatTime(timeLeft)}
        </div>
      </div>

      {/* Progress bar */}
      <div className="quiz-progress-bar">
        <div
          className="quiz-progress-fill"
          style={{
            width: `${((currentQ + 1) / questions.length) * 100}%`,
          }}
        />
      </div>

      {/* Question dots */}
      <div className="quiz-dots">
        {questions.map((question, i) => (
          <button
            key={question.id}
            className={`quiz-dot ${i === currentQ ? "dot-active" : ""} ${
              answers[question.id] !== undefined
                ? answers[question.id] === question.correct
                  ? "dot-correct"
                  : "dot-wrong"
                : ""
            }`}
            onClick={() => {
              setShowExplanation(false);
              setCurrentQ(i);
            }}
            title={`Question ${i + 1}`}
          >
            {i + 1}
          </button>
        ))}
      </div>

      {/* Question card */}
      <div className="quiz-card">
        <div className="quiz-module-label">{q.module}</div>
        <h2 className="quiz-question">{q.question}</h2>

        <div className="quiz-options">
          {q.options.map((option, i) => {
            let optClass = "quiz-option";
            if (hasAnswered) {
              if (i === q.correct) optClass += " option-correct";
              else if (i === userAnswer) optClass += " option-wrong";
              else optClass += " option-disabled";
            }
            return (
              <button
                key={i}
                className={optClass}
                onClick={() => handleAnswer(q.id, i)}
                disabled={hasAnswered}
              >
                <span className="option-letter">
                  {String.fromCharCode(65 + i)}
                </span>
                <span className="option-text">{option}</span>
              </button>
            );
          })}
        </div>

        {/* Explanation */}
        {showExplanation && hasAnswered && (
          <div
            className={`quiz-explanation ${
              userAnswer === q.correct ? "explanation-correct" : "explanation-wrong"
            }`}
          >
            <div className="explanation-header">
              {userAnswer === q.correct ? (
                <span>✅ Bonne réponse !</span>
              ) : (
                <span>
                  ❌ Mauvaise réponse — La bonne réponse est{" "}
                  <strong>{String.fromCharCode(65 + q.correct)}</strong>
                </span>
              )}
            </div>
            <p>{q.explanation}</p>
          </div>
        )}
      </div>

      {/* Navigation */}
      <div className="quiz-nav">
        <button
          className="quiz-btn quiz-btn-prev"
          onClick={prevQuestion}
          disabled={currentQ === 0}
        >
          ← Précédente
        </button>

        <button className="quiz-btn quiz-btn-finish" onClick={finishQuiz}>
          🏁 Terminer le QCM
        </button>

        <button
          className="quiz-btn quiz-btn-next"
          onClick={nextQuestion}
        >
          {currentQ < questions.length - 1 ? "Suivante →" : "Voir les résultats →"}
        </button>
      </div>
    </div>
  );
}

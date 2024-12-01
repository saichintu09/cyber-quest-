let currentQuestionIndex = 0;
let score = 0;
let questions = [];

// Function to load questions from the server
function loadQuestions() {
    fetch('/get-questions')
        .then(response => response.json())
        .then(data => {
            questions = data.questions;
            showQuestion();
        });
}

// Function to show the current question
function showQuestion() {
    if (currentQuestionIndex < questions.length) {
        let question = questions[currentQuestionIndex];
        document.getElementById('question').innerText = question.question;
        let answerButtons = document.getElementById('answer-buttons');
        answerButtons.innerHTML = '';

        question.answers.forEach((answer, index) => {
            let button = document.createElement('button');
            button.classList.add('answer-btn');
            button.innerText = answer.text;
            button.onclick = () => checkAnswer(answer, index);
            answerButtons.appendChild(button);
        });
    } else {
        showResult();
    }
}

// Function to check the user's answer
function checkAnswer(selectedAnswer, index) {
    let question = questions[currentQuestionIndex];
    if (selectedAnswer.isCorrect) {
        score++;
    }
    
    // Show explanation if available
    let explanationContainer = document.getElementById('explanation');
    explanationContainer.innerText = question.explanation || 'No explanation available.';
    
    currentQuestionIndex++;
    setTimeout(showQuestion, 2000);  // Show next question after 2 seconds
}

// Function to display the result at the end
function showResult() {
    document.getElementById('quiz-container').style.display = 'none';
    let resultContainer = document.getElementById('result-container');
    resultContainer.innerHTML = `You scored ${score} out of ${questions.length}`;
    resultContainer.style.display = 'block';
}

window.onload = loadQuestions;

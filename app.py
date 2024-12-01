from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session to work

# Questions organized by difficulty level
questions = {
    "easy": [
        {
            "question": "What is a firewall in cybersecurity?",
            "options": ["A device to store data", "A barrier to protect a network", "A type of malware", "A web browser"],
            "correct_answer": "A barrier to protect a network",
            "explanation": "A firewall is a network security system designed to monitor and control incoming and outgoing network traffic."
        },
        {
            "question": "Which of these is a type of malware?",
            "options": ["Windows", "MacOS", "Trojan", "Linux"],
            "correct_answer": "Trojan",
            "explanation": "A Trojan horse is a type of malware that is often disguised as legitimate software."
        }
    ],
    "medium": [
        {
            "question": "What does the term 'phishing' refer to?",
            "options": ["A type of email attack", "A technique to steal data", "A form of malware", "A security vulnerability"],
            "correct_answer": "A type of email attack",
            "explanation": "Phishing is an attack method where cybercriminals trick individuals into revealing sensitive information via fraudulent emails."
        },
        {
            "question": "Which of the following is an example of a DDoS attack?",
            "options": ["SQL Injection", "Denial of Service", "Phishing", "Man-in-the-middle"],
            "correct_answer": "Denial of Service",
            "explanation": "A Distributed Denial of Service (DDoS) attack aims to overwhelm a server or network, making it unavailable to users."
        }
    ],
    "hard": [
        {
            "question": "What is a zero-day vulnerability?",
            "options": ["A type of virus", "A vulnerability discovered by hackers", "A vulnerability that is exploited before the developer fixes it", "A malware attack"],
            "correct_answer": "A vulnerability that is exploited before the developer fixes it",
            "explanation": "A zero-day vulnerability is a flaw in software that is exploited by attackers before the developer has a chance to patch it."
        },
        {
            "question": "Which cryptographic algorithm is considered quantum-resistant?",
            "options": ["RSA", "Elliptic Curve", "Lattice-based", "AES"],
            "correct_answer": "Lattice-based",
            "explanation": "Lattice-based cryptography is considered quantum-resistant because it is believed to be difficult for quantum computers to break."
        }
    ]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start-quiz', methods=['GET', 'POST'])
def start_quiz():
    if 'current_level' not in session:
        session['current_level'] = 'easy'
        session['score'] = 0
        session['answered_questions'] = 0

    level = session['current_level']
    current_question = questions[level][session['answered_questions']]

    if request.method == 'POST':
        user_answer = request.form.get('answer')
        correct_answer = current_question['correct_answer']
        
        if user_answer == correct_answer:
            session['score'] += 1
            session['answered_questions'] += 1
        else:
            session['answered_questions'] += 1

        if session['answered_questions'] == len(questions[level]):
            # Move to the next level if current level is completed
            if level == 'easy':
                session['current_level'] = 'medium'
            elif level == 'medium':
                session['current_level'] = 'hard'

            return redirect(url_for('show_results'))

    return render_template('quiz.html', question=current_question, level=level)

@app.route('/show-results')
def show_results():
    level = session['current_level']
    total_questions = sum(len(questions[level]) for level in questions)
    return render_template('results.html', score=session['score'], total_questions=total_questions)

if __name__ == '__main__':
    app.run(debug=True)

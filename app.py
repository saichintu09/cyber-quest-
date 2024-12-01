from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Quiz route
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Handle quiz submission
        answers = request.form
        score = 0
        correct_answers = {
            "q1": "b",
            "q2": "a",
            "q3": "c"
        }
        for question, answer in correct_answers.items():
            if answers.get(question) == answer:
                score += 1
        return render_template('quiz.html', score=score, completed=True)
    return render_template('quiz.html', completed=False)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

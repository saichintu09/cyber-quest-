from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    # You can add your quiz logic here
    return render_template('quiz.html')

if __name__ == '__main__':
    app.run(debug=True)

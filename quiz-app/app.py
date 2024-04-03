from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample quiz questions
questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['London', 'Paris', 'Berlin', 'Madrid'],
        'answer': 'Paris'
    },
    {
        'question': 'What is 2 + 2?',
        'options': ['3', '4', '5', '6'],
        'answer': '4'
    }
]

# Index route
@app.route('/')
def index():
    return render_template('index.html', questions=questions)

# Quiz route
@app.route('/quiz', methods=['POST'])
def quiz():
    score = 0
    for i, question in enumerate(questions):
        selected_option = request.form.get(f'question-{i}')
        if selected_option == question['answer']:
            score += 1
    return render_template('result.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)

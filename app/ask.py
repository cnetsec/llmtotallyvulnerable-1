from flask import Blueprint, render_template, request
from app.model import GPT2Generator

ask_blueprint = Blueprint('ask', __name__)

generator = GPT2Generator()

@ask_blueprint.route('/', methods=['GET', 'POST'])
def ask_question():
    if request.method == 'POST':
        question = request.form['question']
        answer = generator.generate_response(question)
        return render_template('ask.html', question=question, answer=answer)
    return render_template('ask.html')


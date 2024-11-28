
from flask import Flask, render_template, request, flash
from werkzeug.utils import redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfajskfhkreuityerihgdgklj'


@app.route('/')
def home():
    return render_template('index.html')

app.route('/home')
def red_home():
    return redirect('/')


@app.route('/form_feedback', methods=["POST", "GET"])
def contacts():
    return render_template('form_feedback.html', title='Обратная связь')

# @app.route('/feedback_handler', methods=['POST'])
# def feed_hand():
#     username = request.form['name']
#     email = request.form['email']
#     phone = request.form['phone']

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title="Страница не найдена")


if __name__ == "__main__":
    app.run(debug=True)
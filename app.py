from flask import Flask, render_template
from forms import LoginForm

app = Flask(__name__)

@app.route('/')
def index():
    tasks = ["Day 2", "Learning Jinja", "Building my portfolio"]
    return render_template('index.html', task_list = tasks)

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form_fields = form)


if __name__ == "__main__":
    app.run(debug=True)
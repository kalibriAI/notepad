from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    text = request.form.get('text')
    if len(text) >= 1:
        with open("notes.txt", "a", encoding='utf-8') as f:
            f.write(f'{"=" * 20} {datetime.now()} {"=" * 20}\n')
            f.write(f'{text}\n')
            f.write(f'{"=" * 68}\n')
    return index()


if __name__ == '__main__':
    app.run()

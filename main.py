from flask import Flask, render_template
from flask_talisman import Talisman

app = Flask(__name__)
Talisman(app)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

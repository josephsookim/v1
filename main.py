from flask import Flask, render_template
from flask_talisman import Talisman

app = Flask(__name__)

csp = {
    'default-src': [
        '\'self\'',
        'cdnjs.cloudflare.com',
        'cdn.jsdelivr.net',
    ],
    'script-src': [
        '\'self\'',
        '\'unsafe-inline\',
        'cdn.jsdelivr.net',
        'ajax.googleapis.com',
    ],
}

Talisman(
    app,
    content_security_policy=csp,
)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

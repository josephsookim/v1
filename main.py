from flask import Flask, render_template
from flask_talisman import Talisman

app = Flask(__name__)

csp = {
    'script-src': [
        '\'self\'',
        'cdnjs.cloudflare.com',
        'ajax.googleapis.com',
        'cdn.jsdelivr.net',
        'https://www.google-analytics.com',
        'https://ssl.google-analytics.com',
    ],
    'img-src': [
        '\'self\'',
        'https://www.google-analytics.com',
    ],
    'connect-src': [
        '\'self\'',
        'https://www.google-analytics.com',
    ],
}

Talisman(app, content_security_policy=csp)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

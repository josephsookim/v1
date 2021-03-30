from flask import Flask, render_template
from flask_talisman import Talisman

app = Flask(__name__)

csp = {
    'default-src': [
        '\'self\'',
    ],
    'script-src': [
        '\'self\'',
        '\'unsafe-inline\'',
        'cdn.jsdelivr.net',
        'ajax.googleapis.com',
        'https://www.google-analytics.com',
        'https://ssl.google-analytics.com',
        'https://www.googletagmanager.com',
    ],
    'style-src': [
        '\'self\'',
        '\'unsafe-inline\'',
        'cdnjs.cloudflare.com',
        'cdn.jsdelivr.net',
    ],
    'font-src': [
        '\'self\'',
        'cdnjs.cloudflare.com',
    ],
    'img-src': [
        '\'self\'',
        'https://www.google-analytics.com',
        'www.googletagmanager.com'
    ],
    'connect-src': [
        '\'self\'',
        'https://www.google-analytics.com',
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

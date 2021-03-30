from flask import Flask, render_template
from flask_talisman import Talisman

app = Flask(__name__)

csp = {
    'default-src': [
        '\'self\'',
        'cdnjs.cloudflare.com',
        'ajax.googleapis.com',
        'cdn.jsdelivr.net',
        'googletagmanager.com'
    ]
}

Talisman(app, content_security_policy=csp)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

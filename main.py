from flask import Flask, render_template
from flask_talisman import Talisman

app = Flask(__name__)

csp = {
    'default-src': [
        '\'self\'',
        'cdnjs.cloudflare.com',
        'ajax.googleapis.com',
        'cdn.jsdelivr.net',
    ],
    'script-src': [
        '\'self\'',
        'https://www.googletagmanager.com',
        'https://www.google-analytics.com',
        'https://ssl.google-analytics.com',
    ],
    'img-src': [
        '\'self\'',
        'www.googletagmanager.com',
        'https://www.google-analytics.com',
    ],
    'connect-src': [
        '\'self\'',
        'https://www.google-analytics.com',
    ],
}

'''
'\'self\'',
'cdnjs.cloudflare.com',
'ajax.googleapis.com',
'cdn.jsdelivr.net',
'''

Talisman(
    app,
    content_security_policy=csp,
    content_security_policy_nonce_in=['script-src']
)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

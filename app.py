import os

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello Flask from alpine-linux!'

@app.route('/json', methods=["POST"])
def test():
    return 'this should appear on every POST request to 0.0.0.0:5000/json'


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

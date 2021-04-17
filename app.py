import os
import string

from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello Flask from alpine-linux!'

@app.route('/postjson', methods=["POST"])
def normalize():
    # get request body
    data_request = request.get_json(force=True)
    
    # normalize
    # force lowercase
    # remove any non-letter, non-digit characters
    new_data = {}
    for key, value in data_request.items():
        new_data.update({
            key.lower()
            .translate(str.maketrans('', '', string.punctuation)) 
            : value,})

    return jsonify(new_data)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

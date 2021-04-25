import flask
from flask import Flask, request, Response
from flask_cors import CORS


app = Flask(__name__)
app.config['DEBUG'] = True
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route("/api/compile", methods=['POST'])
def compile():
    if request.method == 'POST':
        d = request.json
        if 'data' not in d:
            return Response("data to compile not found in body", status=400)
        toCompile = d['data']
        return flask.jsonify({'asm': 'yolo'})


if __name__ == "__main__":
    app.run(debug=True)

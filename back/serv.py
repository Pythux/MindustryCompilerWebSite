import flask
from flask import Flask, request, Response
from flask_cors import CORS

# import compiler here:
from compiler import CompilationException
from compiler.yacc.mainYacc import runYacc


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
        try:
            compiled = runYacc(toCompile, clearContext=True)
            return flask.jsonify({'asm': compiled})
        except CompilationException as e:
            return flask.jsonify({'error': str(e)})


# for gunicorn standard entry-point
application = app
__all__ = [application]


if __name__ == "__main__":
    app.run()

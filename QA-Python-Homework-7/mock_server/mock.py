#!/usr/bin/env python3


from flask import Flask, jsonify, request
from werkzeug.serving import WSGIRequestHandler
from settings import *
import threading
import logging
import click



app = Flask('MockServer')
SURNAME_DATA = {}

@app.route('/get_user/<name>', methods=['GET'])
def get_surname(name):
    if surname := SURNAME_DATA.get(name):
        return jsonify(surname), 200
    else:
        return jsonify(f'Surname for user "{name}" not found'), 404

@app.route('/put_user/<name>', methods=['PUT'])
def put_surname(name):
    if json := request.json:
        if SURNAME_DATA.get(name):
            SURNAME_DATA[name] = json['surname']
            return jsonify(json['surname']), 200
        else:
            SURNAME_DATA[name] = json['surname']
            return jsonify({'name':name, 'surname':json['surname']}), 201
    return jsonify('Request body not passed'), 400

@app.route('/delete_user/<name>', methods=['DELETE'])
def delete_record(name):
    if SURNAME_DATA.get(name):
        SURNAME_DATA.pop(name)
        return jsonify('Successful deletion'), 204
    else:
        return jsonify(f'Surname for user "{name}" not found'), 404

@app.route('/post_user', methods=['POST'])
def post_surname():
    if json := request.json:
        SURNAME_DATA[json['name']] = json['surname']
        return jsonify(json), 201
    return jsonify('Request body not passed'), 400

@app.route('/shutdown')
def shutdown():
    shutdown_mock()
    return jsonify(f'Ok, exiting'), 200

def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()

def run_server():
    WSGIRequestHandler.protocol_version = 'HTTP/1.1'
    threading.Thread(target=app.run, kwargs={
        'host':MOCK_HOST,
        'port':MOCK_PORT,
    }).start()

def flask_redirect_stderr(root):
    logger = logging.getLogger('werkzeug')
    logger.removeHandler(logging.StreamHandler())
    handler = logging.FileHandler(root,'w')
    handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s"))
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)

def flask_redirect_stdout(root):
    def echo(text, **args):
        with open(root,'a') as f:
            print(text, file=f)
    def secho(text, **args):
        echo(text)
    click.echo = echo
    click.secho = secho

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=8080,
        debug=True
    )
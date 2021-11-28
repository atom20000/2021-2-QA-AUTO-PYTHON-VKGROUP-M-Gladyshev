#!/usr/bin/env python3


from flask import Flask, jsonify, request, Response
from werkzeug.serving import WSGIRequestHandler
import threading

from flask.views import View
from functools import partial, update_wrapper

from settings import *

class Glask(Flask):

    def __init__(self, *args, **kwargs):
        Flask.__init__(self, *args, **kwargs)
    
    def route(self, rule, **options):
        apply_self = lambda f: update_wrapper(partial(f, self=None), f) 
        decorator = Flask.route(self, rule, **options)    
        return  lambda *args, **kwargs: decorator(apply_self(*args, **kwargs))

app = Flask('MockServer')

SURNAME_DATA = {}

#class MockServer():

#def __init__(self, host, port):
#    self.host = host
#    self.port = port
#    self.run_server

@app.route('/get_user/<name>', methods=['GET'])
def get_surname(name):
    #import pdb; pdb.set_trace()
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
            return jsonify(json), 201
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
    #import pdb; pdb.set_trace()
    if json := request.json:
        SURNAME_DATA[json['name']] = json['surname']
        return jsonify(json), 201
    return jsonify('Request body not passed'), 400

#def shutdown_server():
#    terminate_func = request.environ.get('werkzeug.server.shutdown')
#    if terminate_func:
#        terminate_func()

@app.route('/shutdown')
def shutdown():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()
    return jsonify(f'Ok, exiting'), 200

def run_server():
    WSGIRequestHandler.protocol_version = 'HTTP/1.1'
    threading.Thread(target=app.run, kwargs={
        'host':MOCK_HOST,
        'port':MOCK_PORT,
        #'debug':True
    }).start()


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=8080,
        debug=True
    )
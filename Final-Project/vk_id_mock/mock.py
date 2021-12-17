#!/usr/bin/env/python3


from flask import Flask, jsonify
from werkzeug.serving import WSGIRequestHandler
import signal
import os

from werkzeug.wrappers import request


app = Flask('VK_ID_Mock')
VK_ID_DATA = {}

@app.route('/vk_id/<username>', methods=['GET'])
def get_id(username):
    if vk_id := VK_ID_DATA.get(username):
        return jsonify({'vk_id': vk_id}), 200
    else:
        return jsonify({}), 404

@app.route('/vk_id/<username>', methods=['POST'])
def post_id(username):
    if json := request.json:
        if VK_ID_DATA.get(username):
            return jsonify('Already exists'), 400
        else:
            VK_ID_DATA[username] = json[username]
            return jsonify({username:json[username]}), 201
    else:
        return jsonify('Request body not passed'), 400

@app.route('/vk_id/<username>', methods=['PUT'])
def put_id(username):
    if json := request.json:
        if VK_ID_DATA.get(username):
            VK_ID_DATA[username] = json[username]
            return jsonify({username:json[username]}), 200
        else:
            VK_ID_DATA[username] = json[username]
            return jsonify({username:json[username]}), 201
    else:
        return jsonify('Request body not passed'), 400

@app.route('/vk_id/<username>', methods=['DELETE'])
def delete_id(username):
    if VK_ID_DATA.get(username):
        VK_ID_DATA.pop(username)
        return jsonify('Successful deletion'), 204
    else:
         return jsonify(f'ID for "{username}" not found'), 404

class ServerTerminationError(Exception):
    pass

def exit_gracefully(signum,frame):
    raise ServerTerminationError()

signal.signal(signal.SIGINT, exit_gracefully)
signal.signal(signal.SIGTERM, exit_gracefully)

if __name__ == '__main__':
    WSGIRequestHandler.protocol_version = 'HTTP/1.1'
    try:
        app.run(
            host=os.environ.get('HOST'),
            port=os.environ.get('PORT')
        )
    except ServerTerminationError:
        pass

         
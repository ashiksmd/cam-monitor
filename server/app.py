#!/usr/bin/env python
from flask import Flask, render_template, Response
from OpenSSL import SSL
import pickle
from camera import Camera
import crypt

#import unsafe-routes

app = Flask(__name__)

@app.route('/snapshot-raw')
def snapshotRaw():
    cam = Camera()
    frame = cam.get_frame()
    frameString = pickle.dumps(frame)
    encryptedResponse = crypt.Encrypt(frameString)
    return pickle.dumps(encryptedResponse)

if __name__ == '__main__':
    context = SSL.Context(SSL.SSLv23_METHOD)
    context.use_privatekey_file('certs/server.key')
    context.use_certificate_file('certs/server.crt')
    app.run(host='0.0.0.0', port=12344, debug=True, ssl_context=context)

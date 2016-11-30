#!/usr/bin/env python
from flask import Flask, render_template, Response
from OpenSSL import SSL
import pickle
from camera import Camera
import crypt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame_as_jpg()
        if frame is None: continue
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/snapshot')
def snapshot():
    cam = Camera()
    frame = cam.get_frame_as_jpg()
    return Response(frame, mimetype='image/jpeg')

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

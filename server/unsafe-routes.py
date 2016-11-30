"""
These routes can be used to test from localhost, but I would not
recommend using these over a network, as that would give outsiders
access to your webcam feed
"""

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

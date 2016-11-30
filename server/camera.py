import cv2

class Camera:
    def __init__(self):
        self.cam = cv2.VideoCapture()
        self.cam.open(0)
        
    def __del__(self):
        self.cam.release()
        
    def get_frame_as_jpg(self):
        img = self.get_frame()
        (_, encoded) = cv2.imencode(".jpg", img)
        return encoded.tostring()

    def get_frame(self):
        (_, img) = self.cam.read()
        (_, img) = self.cam.read()   # Take 2 frames to ignore the one in buffer, which may be old
        return img

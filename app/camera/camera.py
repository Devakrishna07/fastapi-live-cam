import cv2
from app.core.config import CAMERA_INDEX, FRAME_WIDTH, FRAME_HEIGHT

class VideoCamera:
    def __init__(self):
        self.cap = cv2.VideoCapture(CAMERA_INDEX)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

    def get_frame(self):
        success, frame = self.cap.read()
        if not success:
            return None

        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

    def release(self):
        self.cap.release()
from app.camera.camera import VideoCamera
import time

camera = VideoCamera()

def generate_stream():
    while True:
        frame = camera.get_frame()
        if frame is None:
            continue

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        time.sleep(0.05)
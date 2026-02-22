from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.services.stream_service import generate_stream

router = APIRouter()

@router.get("/video_feed")
def video_feed():
    return StreamingResponse(
        generate_stream(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )
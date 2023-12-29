from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from app.schema.chat import ChatRequest
from app.service.chat_service import ChatService

router = APIRouter()
chat_service = ChatService()

@router.post("/api/v1/chat-completion")
def chat(request: ChatRequest):
  try:
    return StreamingResponse(chat_service.chat(request.question))
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

from pydantic import BaseModel
from typing import List
class Delta(BaseModel):
    content: str

class Choice(BaseModel):
    delta: Delta

class Auth(BaseModel):
  user_id: str

class ChatRequest(BaseModel):
  auth: Auth
  question: str

class ChatResponse(BaseModel):
    choices: List[Choice]
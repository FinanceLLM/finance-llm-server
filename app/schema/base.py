from pydantic import BaseModel

class StatusInfo(BaseModel):
  status: int
  message: str

class BaseResponse(BaseModel):
  result: str
  statusinfo: StatusInfo
from typing import Optional
from pydantic import BaseModel

class ResponseErrorCode(BaseModel):
    error_code: int
    message: Optional[str]
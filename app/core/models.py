from pydantic import BaseModel
from typing import Optional

class AskResponse(BaseModel):
    answer: str
    contents: list
    chat_id: str
    converstion_id: str
    error: Optional[str] = None
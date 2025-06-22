from typing import List, Optional
from pydantic import BaseModel

class ChatState(BaseModel):
    messages: List[str] = []
    user_input: Optional[str] = None
    search_results: Optional[List[str]] = None
    final_response: Optional[str] = None

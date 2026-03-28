from pydantic import BaseModel
from typing import List, Optional, Dict

class Observation(BaseModel):
    ticket_id: str
    customer_message: str
    history: List[str]
    metadata: Dict

class Action(BaseModel):
    action_type: str
    content: Optional[str] = None
    category: Optional[str] = None

class Reward(BaseModel):
    score: float
    feedback: str

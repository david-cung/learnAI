from typing import Literal
from pydantic import BaseModel, Field

class TicketCreate(BaseModel):
    customer_id: str
    subject: str = Field(min_length=3)
    description: str = Field(min_length=10)
    status: Literal['open', 'closed'] = 'open'

class TicketStatusUpdate(BaseModel):
    status: Literal['open', 'closed']
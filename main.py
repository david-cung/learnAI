from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

tickets: list[dict] = []


class TicketCreate(BaseModel):
    customer_id: str
    subject: str = Field(min_length=3)
    description: str = Field(min_length=10)


@app.post("/tickets", status_code=201)
def create_ticket(ticket: TicketCreate):
    ticket_id = len(tickets) + 1
    ticket = ticket.model_dump()
    ticket["id"] = ticket_id
    ticket["status"] = 'open'
    tickets.append(ticket)
    return ticket

@app.get("/health")
def health():
    return {"status": "healthy"}
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import sqlite3

app = FastAPI()


tickets: list[dict] = []

class TicketCreate(BaseModel):
    customer_id: str
    subject: str = Field(min_length=3)
    description: str = Field(min_length=10)
    # status: string = Field(default='open', regex='^(open|closed)$')

@app.post('/tickets', status_code=201)
def create_ticket(ticket: TicketCreate):
    con = sqlite3.connect('tickets.db')
    con.row_factory = sqlite3.Row
    ticket = ticket.model_dump()
    try:
        cursor = con.execute(
            '''
            insert into tickets (customer_id, subject, description, status) values
                (?, ?, ?, ?)''', 
                (ticket["customer_id"], ticket["subject"], ticket["description"], "open")
        )
        con.commit() 
        row = con.execute('SELECT * FROM tickets where id = ?', (cursor.lastrowid,)
                          ).fetchone()
        return cursor.lastrowid
    finally:
        con.close()
    

@app.get('/tickets/{ticket_id}')
def get_ticket(ticket_id: int):
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket
    raise HTTPException(status_code=404, detail="Ticket not found")

@app.get('/tickets')
def get_tickets(status: str | None = None):
    if status is not None:
        return [ticket for ticket in tickets if ticket["status"] == status]
    # list_ticket = []
    # for ticket in tickets:
    #     if ticket["status"] == status:
    #         list_ticket.append(ticket)
    # return list_ticket
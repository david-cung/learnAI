from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import sqlite3
from pathlib import Path

DB_Path = Path(__file__).with_name('tickets.db')

app = FastAPI()

class TicketCreate(BaseModel):
    customer_id: str
    subject: str = Field(min_length=3)
    description: str = Field(min_length=10)
    # status: string = Field(default='open', regex='^(open|closed)$')

@app.get('/health')
def health():
    return {"status": "ok"}

@app.post('/tickets', status_code=201)
def create_ticket(ticket: TicketCreate):
    conn = sqlite3.connect(DB_Path)
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO tickets (customer_id, subject, description, status)
            VALUES (?, ?, ?, ?)
        ''', (ticket.customer_id, ticket.subject, ticket.description, 'open'))
        conn.commit()
    finally:
        conn.close()

    ticket_id = cursor.lastrowid
    return ticket_id

@app.get('/tickets/{ticket_id}')
def get_ticket(ticket_id: int):
    conn = sqlite3.connect(DB_Path)
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM tickets WHERE id = ?', (ticket_id,))
        ticket = cursor.fetchone()
    finally:
        conn.close()

    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return {
        "id": ticket[0],
        "customer_id": ticket[1],
        "subject": ticket[2],
        "description": ticket[3],
        "status": ticket[4]
    }

@app.get('/tickets')
def get_tickets(status: str | None = None):
    conn = sqlite3.connect(DB_Path)
    cursor = conn.cursor()
    try:
        if status is not None:
            cursor.execute('SELECT * FROM tickets WHERE status = ?', (status,))
        else:
            cursor.execute('SELECT * FROM tickets')
        tickets = cursor.fetchall()
    finally:
        conn.close()
    return [
        {
            "id": ticket[0],
            "customer_id": ticket[1],
            "subject": ticket[2],
            "description": ticket[3],
            "status": ticket[4]
        }
        for ticket in tickets
    ]

def init_db():
    conn = sqlite3.connect(DB_Path)
    cursor = conn.cursor()
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id TEXT NOT NULL,
                subject TEXT NOT NULL,
                description TEXT NOT NULL,
                status TEXT NOT NULL CHECK(status IN ('open', 'closed'))
            )
        ''')
        conn.commit()
    finally:
        conn.close()
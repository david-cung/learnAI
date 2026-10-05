
from fastapi import APIRouter, HTTPException
import database
from schemas import TicketCreate, TicketStatusUpdate

router = APIRouter(prefix="/tickets", tags=["tickets"])

@router.get('/health')
def health():
    return {"status": "ok"}

@router.post("", status_code=201)
def create_ticket(ticket: TicketCreate):
    conn = database.connect_db()
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

@router.get('/{ticket_id}')
def get_ticket(ticket_id: int):
    conn = database.connect_db()
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

@router.get('')
def get_tickets(status: str | None = None):
    conn = database.connect_db()
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

@router.patch('/{ticket_id}/status')
def update_ticket_status(ticket_id: int, ticket_update: TicketStatusUpdate):
    conn = database.connect_db()
    try:
        cursor = conn.cursor()
        ticketExists = cursor.execute('SELECT * FROM tickets WHERE id = ?', (ticket_id,)).fetchone()
        if ticketExists is None:
            raise HTTPException(status_code=404, detail="Ticket not found")
        cursor.execute('UPDATE tickets SET status = ? WHERE id = ?', (ticket_update.status, ticket_id))
        conn.commit()
        return {"message": "Ticket status updated successfully"}
    finally:
        conn.close()

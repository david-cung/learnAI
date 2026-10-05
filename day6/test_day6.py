import pytest
from fastapi.testclient import TestClient

import database
import main

@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(database, "DB_PATH", tmp_path / "tickets.db")
    
    with TestClient(main.app) as test_client:
        yield test_client

def test_create_and_get_ticket(client):
    payload = {
        "customer_id": "test",
        "subject": "Test Ticket",
        "description": "This is a test ticket."
    }

    response = client.post("/tickets", json=payload)
    print("Response:", response.json())
    assert response.status_code == 201, response.json()
    ticket_id = response.json()
    print("Created ticket:", ticket_id)

    response = client.get(f"/tickets/{ticket_id}")
    assert response.status_code == 200
    retrieved = response.json()
    assert retrieved["id"] == ticket_id

def test_update_ticket_status(client):
    # Create a ticket first
    payload = {
        "customer_id": "test",
        "subject": "Test Ticket for Update",
        "description": "This is a test ticket for update."
    }
    response = client.post("/tickets", json=payload)
    print("Create ticket response:",response.status_code, response.json())
    assert response.status_code == 201, response.json()
    ticket_id = response.json()

    # Update the ticket status
    update_payload = {
        "status": "closed"
    }
    response = client.patch(f"/tickets/{ticket_id}/status", json=update_payload)
    assert response.status_code == 200

    # Retrieve the updated ticket
    response = client.get(f"/tickets/{ticket_id}")
    assert response.status_code == 200
    retrieved = response.json()
    assert retrieved["status"] == "closed"
    
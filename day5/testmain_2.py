import pytest
from fastapi.testclient import TestClient
import main

@pytest.fixture
def client(tmp_path, monkeypatch):
    test_db = tmp_path / "test_tickets.db"
    monkeypatch.setattr(main, "DB_Path", test_db)

    main.init_db()

    with TestClient(main.app) as test_client:
        yield test_client

def test_create_and_get_ticket(client):
    payload = {
        "customer_id": "test",
        "subject": "Test Ticket",
        "description": "This is a test ticket."
    }

    response = client.post("/tickets", json=payload)

    assert response.status_code == 201, response.json()
    ticket_id = response.json()
    print("Created ticket:", ticket_id)
    # ticket_id = created["id"]

    response = client.get(f"/tickets/{ticket_id}")
    assert response.status_code == 200
    retrieved = response.json()
    assert retrieved["id"] == ticket_id

def test_get_not_found_ticket(client):
    response = client.get("tickets/9999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Ticket not found"}

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

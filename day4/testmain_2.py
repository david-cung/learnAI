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
        "customer_id": 1,
        "subject": "Test Ticket",
        "description": "This is a test ticket."
    }

    response = client.post("/tickets", json=payload)

    assert response.status_code == 201
    created = response.json()
    ticket_id = created["id"]

    response = client.get(f"/tickets/{ticket_id}")
    assert response.status_code == 200
    retrieved = response.json()
    assert retrieved == created
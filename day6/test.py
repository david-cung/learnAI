import pytest
from fastapi.testclient import TestClient

import database
import main

@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(database, "DB_PATH", tmp_path / "tickets.db")
    
    with TestClient(main.app) as test_client:
        yield test_client
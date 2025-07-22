import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from fastapi.testclient import TestClient
from unittest.mock import Mock
import requests

from main import app

client = TestClient(app)

def test_chat_endpoint(monkeypatch):
    mock_response = Mock()
    mock_response.json.return_value = {"id": "chatcmpl-123"}
    monkeypatch.setattr(requests, "post", lambda *a, **kw: mock_response)

    res = client.post("/chat", json={"message": "Hello"})
    assert res.status_code == 200
    assert res.json() == {"id": "chatcmpl-123"}

from fastapi.testclient import TestClient


def test_create_and_read_ticket(client: TestClient) -> None:
    created = client.post(
        "/tickets",
        json={"title": "Synthetic incident", "description": "A fictional queue is delayed."},
    )
    assert created.status_code == 201
    ticket = created.json()
    assert ticket["title"] == "Synthetic incident"

    fetched = client.get(f"/tickets/{ticket['id']}")
    assert fetched.status_code == 200
    assert fetched.json() == ticket


def test_unknown_ticket_returns_404(client: TestClient) -> None:
    response = client.get("/tickets/999")
    assert response.status_code == 404


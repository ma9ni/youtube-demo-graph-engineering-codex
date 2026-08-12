from fastapi.testclient import TestClient


def test_create_and_read_ticket(client: TestClient) -> None:
    created = client.post(
        "/tickets",
        json={"title": "Synthetic incident", "description": "A fictional queue is delayed."},
    )
    assert created.status_code == 201
    ticket = created.json()
    assert ticket["title"] == "Synthetic incident"
    assert ticket["status"] == "pending"

    fetched = client.get(f"/tickets/{ticket['id']}")
    assert fetched.status_code == 200
    assert fetched.json() == ticket


def test_unknown_ticket_returns_404(client: TestClient) -> None:
    response = client.get("/tickets/999")
    assert response.status_code == 404


def test_valid_status_transitions_are_persisted(client: TestClient) -> None:
    ticket = client.post(
        "/tickets", json={"title": "Demo ticket", "description": "Synthetic workload."}
    ).json()

    in_progress = client.patch(
        f"/tickets/{ticket['id']}/status", json={"status": "in_progress"}
    )
    assert in_progress.status_code == 200
    assert in_progress.json()["status"] == "in_progress"

    done = client.patch(f"/tickets/{ticket['id']}/status", json={"status": "done"})
    assert done.status_code == 200
    assert done.json()["status"] == "done"
    assert client.get(f"/tickets/{ticket['id']}").json()["status"] == "done"


def test_invalid_transition_is_rejected_without_mutation(client: TestClient) -> None:
    ticket = client.post(
        "/tickets", json={"title": "Demo ticket", "description": "Synthetic workload."}
    ).json()

    rejected = client.patch(f"/tickets/{ticket['id']}/status", json={"status": "done"})
    assert rejected.status_code == 409
    assert client.get(f"/tickets/{ticket['id']}").json()["status"] == "pending"


def test_unknown_status_is_rejected(client: TestClient) -> None:
    ticket = client.post(
        "/tickets", json={"title": "Demo ticket", "description": "Synthetic workload."}
    ).json()
    response = client.patch(
        f"/tickets/{ticket['id']}/status", json={"status": "definitely-not-real"}
    )
    assert response.status_code == 422

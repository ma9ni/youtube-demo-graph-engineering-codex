from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, status

from app.database import connect, initialize_database
from app.schemas import Ticket, TicketCreate, TicketStatus, TicketStatusUpdate


ALLOWED_TRANSITIONS = {
    TicketStatus.PENDING: TicketStatus.IN_PROGRESS,
    TicketStatus.IN_PROGRESS: TicketStatus.DONE,
}


@asynccontextmanager
async def lifespan(_: FastAPI):
    initialize_database()
    yield


app = FastAPI(
    title="Neutral Ticket API",
    description="Public synthetic project for a Graph Engineering experiment.",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/tickets", response_model=Ticket, status_code=status.HTTP_201_CREATED)
def create_ticket(payload: TicketCreate) -> Ticket:
    with connect() as connection:
        cursor = connection.execute(
            "INSERT INTO tickets (title, description) VALUES (?, ?)",
            (payload.title, payload.description),
        )
        row = connection.execute(
            "SELECT id, title, description, status FROM tickets WHERE id = ?",
            (cursor.lastrowid,),
        ).fetchone()
    if row is None:
        raise HTTPException(status_code=500, detail="Ticket creation failed")
    return Ticket(**dict(row))


@app.get("/tickets", response_model=list[Ticket])
def list_tickets() -> list[Ticket]:
    with connect() as connection:
        rows = connection.execute(
            "SELECT id, title, description, status FROM tickets ORDER BY id"
        ).fetchall()
    return [Ticket(**dict(row)) for row in rows]


@app.get("/tickets/{ticket_id}", response_model=Ticket)
def get_ticket(ticket_id: int) -> Ticket:
    with connect() as connection:
        row = connection.execute(
            "SELECT id, title, description, status FROM tickets WHERE id = ?", (ticket_id,)
        ).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return Ticket(**dict(row))


@app.patch("/tickets/{ticket_id}/status", response_model=Ticket)
def update_ticket_status(ticket_id: int, payload: TicketStatusUpdate) -> Ticket:
    with connect() as connection:
        current = connection.execute(
            "SELECT id, title, description, status FROM tickets WHERE id = ?", (ticket_id,)
        ).fetchone()
        if current is None:
            raise HTTPException(status_code=404, detail="Ticket not found")

        current_status = TicketStatus(current["status"])
        if ALLOWED_TRANSITIONS.get(current_status) != payload.status:
            raise HTTPException(
                status_code=409,
                detail=f"Transition {current_status.value} -> {payload.status.value} is not allowed",
            )

        connection.execute(
            "UPDATE tickets SET status = ? WHERE id = ?", (payload.status.value, ticket_id)
        )
        updated = connection.execute(
            "SELECT id, title, description, status FROM tickets WHERE id = ?", (ticket_id,)
        ).fetchone()
    return Ticket(**dict(updated))

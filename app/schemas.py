from enum import StrEnum

from pydantic import BaseModel, Field


class TicketStatus(StrEnum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class TicketCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=3, max_length=500)


class Ticket(BaseModel):
    id: int
    title: str
    description: str
    status: TicketStatus


class TicketStatusUpdate(BaseModel):
    status: TicketStatus

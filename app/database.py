import os
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator


def database_path() -> Path:
    return Path(os.getenv("TICKET_DB_PATH", "demo.db"))


@contextmanager
def connect() -> Iterator[sqlite3.Connection]:
    connection = sqlite3.connect(database_path())
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    finally:
        connection.close()


def initialize_database() -> None:
    with connect() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'pending'
            )
            """
        )
        columns = {
            row["name"] for row in connection.execute("PRAGMA table_info(tickets)").fetchall()
        }
        if "status" not in columns:
            connection.execute(
                "ALTER TABLE tickets ADD COLUMN status TEXT NOT NULL DEFAULT 'pending'"
            )

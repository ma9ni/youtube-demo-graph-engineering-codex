.PHONY: install run test validate reset

install:
	uv sync

run:
	uv run uvicorn app.main:app --reload

test:
	uv run pytest -q

validate:
	uv run ruff check .
	uv run pytest -q

reset:
	rm -f demo.db


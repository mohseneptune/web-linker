.DEFAULT_GOAL := help

virtualenv = .venv
source_dir = src

run-fastapi-app:
	@cd ${source_dir} && uvicorn main:app --reload

up-docker-compose:
	@docker compose up -d

down-docker-compose:
	@docker compose down

pre-commit:
	@git add .
	@pre-commit run -a

help:
	@echo "Usage: make [TARGET ...]"
	@echo ""
	@echo "Targets:"
	@echo "  run-fastapi-app: Run FastAPI app"
	@echo "  up-docker-compose: Up docker-compose"
	@echo "  down-docker-compose: Down docker-compose"
	@echo "  pre-commit: Run pre-commit"
	@echo "  help: Show this help message"

.PHONY: run-fastapi-app up-docker-compose down-docker-compose pre-commit help

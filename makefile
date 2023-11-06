.DEFAULT_GOAL := help

source_dir = src
virtualenv = .venv

cleanup:
	@find . -type d -name '*cache*' ! -path "./$(virtualenv)/*" -exec echo Removing {} \; -exec rm -rf {} +

tree:
	@tree -a -I "$(virtualenv)|.git"

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
	@echo "  cleanup: Cleanup cache"
	@echo "  run-fastapi-app: Run FastAPI app"
	@echo "  up-docker-compose: Up docker-compose"
	@echo "  down-docker-compose: Down docker-compose"
	@echo "  pre-commit: Run pre-commit"
	@echo "  help: Show this help message"

.PHONY: cleanup tree run-fastapi-app up-docker-compose down-docker-compose pre-commit help

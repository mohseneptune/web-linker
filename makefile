.DEFAULT_GOAL := help

source_dir = src
virtualenv = .venv

cleanup:
	@find . -type d \( -path "./$(virtualenv)" -o -path "./docker" \) -prune -o -type d -name '*cache*' -exec echo Removing {} \; -exec rm -rf {} +

tree: cleanup
	@tree -a -I "$(virtualenv)|.git|docker"


run-app:
	@cd ${source_dir} && uvicorn main:app --reload

dc-up:
	@docker compose up -d

dc-down:
	@docker compose down

pre-commit:
	@git add .
	@pre-commit run -a

migrations:
	ifndef m
		$(error m is undefined. Usage: make migrations m="some message")
	endif
	alembic revision --autogenerate -m "$(m)"

migrate:
	alembic upgrade head

downgrade:
	alembic downgrade -1

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  cleanup		- Remove all __pycache__ and .pytest_cache folders"
	@echo "  tree			- Show project tree"
	@echo "  run-app		- Run app"
	@echo "  dc-up			- Run docker-compose up"
	@echo "  dc-down		- Run docker-compose down"
	@echo "  pre-commit		- Run pre-commit"
	@echo "  migrations		- Create migrations"
	@echo "  migrate		- Run migrations"
	@echo "  downgrade		- Downgrade migrations"
	@echo "  help			- Show this help"

.PHONY: cleanup tree run-app dc-up dc-down pre-commit migrations migrate downgrade help

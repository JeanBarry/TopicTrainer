start:
	docker compose -f infrastructure/compose.yaml --env-file=.env up -d

restart:
	docker compose -f infrastructure/compose.yaml --env-file=.env up --build -d

stop:
	docker compose -f infrastructure/compose.yaml --env-file=.env down

logs:
	docker compose -f infrastructure/compose.yaml --env-file=.env logs -f

lint:
	docker exec app sh -c "pylint --rcfile=.pylintrc main.py src/" || true

clean:
	sh scripts/docker-clean.sh
	sh scripts/database-clean.sh

clean-database:
	sh scripts/database-clean.sh

install-local:
	sh scripts/install-local.sh

shell:
	sh scripts/docker-shell.sh

setup: set-hosts set-env

set-hosts:
	sudo sh scripts/setup-hosts.sh

set-env:
	sh scripts/set-env.sh

generate-migration:
	sh scripts/generate-migration.sh

migrate:
	docker exec app sh -c "cd src/database && alembic upgrade head"

rollback:
	docker exec app sh -c "cd src/database && alembic downgrade -1"

playground:
	docker exec app sh -c "cd src/experiments && python3 playground.py"

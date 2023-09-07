start:
	docker compose -f infrastructure/compose.yaml --env-file=.env up -d

restart:
	docker compose -f infrastructure/compose.yaml --env-file=.env up --build -d

stop:
	docker compose -f infrastructure/compose.yaml --env-file=.env down

logs:
	docker compose -f infrastructure/compose.yaml --env-file=.env logs -f

lint:
	docker exec app sh -c "pylint --rcfile=.pylintrc main.py src/"

clean:
	sh scripts/docker-clean.sh

install-local:
	sh scripts/install-local.sh

setup: set-hosts set-env

set-hosts:
	sudo sh scripts/setup-hosts.sh

set-env:
	sh scripts/set-env.sh

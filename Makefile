.PHONY: reset build up down prune

down:
	docker-compose down

prune:
	docker system prune -a --volumes -f

reset: down prune

build:
	docker-compose up -d --remove-orphans

up: build

rebuild: reset build

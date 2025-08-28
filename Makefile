build:
	docker compose build

start:
	docker compose up -d --build
	
up:
	docker compose up -d

down:
	docker compose down

clean:
	docker compose down --volumes --rmi all

log:
	docker compose logs -f

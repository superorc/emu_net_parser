
docker-compose:
	docker-compose up --build

activate_virtualenv:
	rm -rf venv
	virtualenv venv; \
	source venv/bin/activate; \
	pip install -r requirements.txt


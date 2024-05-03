mig:
	python3 manage.py makemigrations
	python3 manage.py migrate
lang:
	python3 manage.py makemessages -l uz -l en
compile:
	python3 manage.py compilemessages --ignore=.venv
flower:
	celery -A root.celery.app flower --port=5001
celery:
	celery -A root worker -l INFO

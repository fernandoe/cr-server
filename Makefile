requirements.txt:
	poetry export --format=requirements.txt --without-hashes --output src/requirements.txt

vercel-dev:
	node node_modules/vercel/dist/index.js dev

pre-commit-all-files:
	pre-commit run --all-files

runserver:
	cd src; python manage.py runserver 0.0.0.0:8000

dreamhost-sync:
	rsync -av --filter '- __pycache__' ./src/ cr:~/cr.controlederisco.com.br

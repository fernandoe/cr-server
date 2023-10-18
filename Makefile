requirements.txt:
	poetry export --format=requirements.txt --without-hashes --output src/requirements.txt

vercel-dev:
	node node_modules/vercel/dist/index.js dev

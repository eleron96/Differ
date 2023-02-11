rebuild: #	соберет и установит пакет
	poetry build
	pip install dist/hexlet_code-0.1.0.tar.gz

lint:
	flake8 gendiff/scripts/
	isort --check-only gendiff/scripts/
	mypy gendiff/scripts/
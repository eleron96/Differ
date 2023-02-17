rebuild: #	соберет и установит пакет
	poetry build
	pip install dist/hexlet_code-0.1.0.tar.gz

lint:
	flake8 gendiff/scripts/
	#isort --check-only gendiff/scripts/
	mypy gendiff/scripts/

coverage test:
	#coverage run --source=gendiff -m pytest tests/test_.py
	#coverage report -m
	coverage run --source=gendiff -m pytest tests/
	coverage report


install requirements:
	pip install -r requirements.txt





install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pip install --upgrade pip
	python3 -m pip install dist/*.whl --force-reinstall


lint:
	poetry run flake8 gendiff

test:
	poetry run pytest tests
	#coverage report -m

coverage:
	poetry run pytest --cov=gendiff tests/ --cov-report xml






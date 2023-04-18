
install:
	poetry install

build:
	rm -rf ./dist
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pip install --upgrade pip
	python3 -m pip install dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff
	poetry run flake8 tests

test:
	poetry run pytest tests
	#coverage report -m

coverage:
	poetry run pytest --cov=gendiff tests/ --cov-report xml






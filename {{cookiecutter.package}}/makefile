.PHONY: clean venv install test format setup style
.ONESHELL: clean venv install test format setup style


package := {{ cookiecutter.package }}

clean:
	rm -rf ./venv

venv:
	python3.12 -m venv ./venv

install:
	. ./venv/bin/activate
	python3.12 -m pip install \
		--no-cache-dir \
		.[dev]
	deactivate

setup: venv
	. ./venv/bin/activate
	python3.11 -m pip install \
		--no-cache-dir \
		-r requirements-dev.txt
	deactivate

test:
	. ./venv/bin/activate
	pytest -s \
		--cov=$(package) \
		--cov-branch \
		--cov-report=term-missing \
		./tests
	deactivate

test-no-install:
	. ./venv/bin/activate
	PYTHONPATH-".:src/"	pytest -s \
		--cov=$(package) \
		--cov-branch \
		--cov-report=term-missing \
		./tests
	deactivate

format:
	. ./venv/bin/activate
	isort ./src/
	black ./src/
	deactivate

style:
	. ./venv/bin/activate
	flake8 ./src/
	pyright ./src/
	deactivate

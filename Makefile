.PHONY: test
test:
	pytest --cov={package_name} -vv tests/
	flake8 {package_name} tests/
	mypy {package_name} --implicit-reexport
	black {package_name} tests/
	isort {package_name} tests/


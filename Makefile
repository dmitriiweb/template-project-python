.PHONY: test
test:
	pytest --cov=template_project_python -vv tests/
	flake8 template_project_python tests/
	mypy template_project_python --implicit-reexport
	black template_project_python tests/
	isort template_project_python tests/

.PHONY: docs-serve
docs-serve:
	mkdocs serve

.PHONY: docs-publish
docs-publish:
	mkdocs mkdocs gh-deploy --force

.PHONY: publish
publish:
	poetry build
	poetry publish

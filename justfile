docs:
	mkdocs serve

publish:
	poetry version patch
	poetry build
	poetry publish

test:
    pytest
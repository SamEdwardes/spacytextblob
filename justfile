build_docs:
	# inspired by https://github.com/pytorch/botorch/blob/master/scripts/build_docs.sh
	# usage: poetry run bash scripts/build_docs.sh
	jupyter nbconvert --to markdown --execute README.ipynb
	jupyter nbconvert --to markdown --execute website/docs/getting_started.ipynb
	jupyter nbconvert --to markdown --execute website/docs/example.ipynb

publish:
	poetry version patch
	poetry build
	poetry publish

test:
    pytest --forked
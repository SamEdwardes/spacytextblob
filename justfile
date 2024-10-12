default:
    @just --list

# ------------------------------------------------------------------------------
# Packaging
# ------------------------------------------------------------------------------

[group('package')]
build:
    rm -rf dist
    uv build

[group('package')]
publish-test:
    rm -rf dist
    uv build
    uv publish --token $(op read "op://Private/Test PyPI/Token") --publish-url https://test.pypi.org/legacy/
    open https://test.pypi.org/project/spacytextblob/

[group('package')]
publish:
    rm -rf dist
    uv build
    uv publish --token $(op read "op://Private/PyPI/Token")
    open https://pypi.org/project/spacytextblob/

# ------------------------------------------------------------------------------
# Lint
# ------------------------------------------------------------------------------

[group('lint')]
format:
    # Sort imports
    uvx ruff check --select I --fix .
    # Format code
    uvx ruff format .

[group('lint')]
lint:
    uvx ruff check .

# ------------------------------------------------------------------------------
# Testing
# ------------------------------------------------------------------------------

[group('tests')]
test version="3.12":
    uv run --python {{version}} --all-extras pytest

[group('tests')]
test-matrix:
    just test 3.9
    just test 3.10
    just test 3.11
    just test 3.12

[group('tests')]
test-pre-release-python:
    # As of 2024-10-12 3.13 is failing
    just test 3.13

[group('tests')]
test-gha:
    gh workflow run pytest.yml --ref $(git branch --show-current)

# ------------------------------------------------------------------------------
# Docs
# ------------------------------------------------------------------------------

[group('docs')]
preview-docs:
    uv run mkdocs serve

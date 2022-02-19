# Contributing

*spacytextblob* is happy to accept contributions from the community. Please review the guidelines below.

## Development environment

### poetry

`poetry` is used to manage python dependencies. See the docs on how to install python [https://python-poetry.org/](https://python-poetry.org/). To activate the poetry virtual environment run the following commands:

```bash
poetry install
poetry shell
```

### just

`just` is used to run scripts. See the just docs for instructions on how to install: [https://github.com/casey/just](https://github.com/casey/just).

## Code formatting

Please use the [black](https://black.readthedocs.io/en/stable/) for formatting code before submitting a PR.

```bash
black spacytextblob
```

## Testing

Please validate that all tests pass before submitting a PR by running:

```bash
pytest
```

## Docs

To build the docs and visually inspect the docs please run:

```bash
just docs
```

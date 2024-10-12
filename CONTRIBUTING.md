# Contributing

*spacytextblob* is happy to accept contributions from the community. Please review the guidelines below.

## Development environment

### uv

`uv` is used to manage python dependencies. Run the following to install `uv`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### just

`just` is used to run scripts. See the just docs for instructions on how to install: [https://github.com/casey/just](https://github.com/casey/just).

## Code formatting

```bash
just format
```

## Testing

Please validate that all tests pass before submitting a PR by running:

```bash
# Test against the latest supported version of Python
just test

# Tet against all supported versions of Python
just test-matrix
```

## Docs

To build the docs and visually inspect the docs please run:

```bash
just preview-docs
```

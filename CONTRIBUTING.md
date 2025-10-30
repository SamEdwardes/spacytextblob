# Contributing

_spacytextblob_ is happy to accept contributions from the community. Please review the guidelines below.

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

## Deployment checklist

Before merging changes into main the following must be completed:

- [ ] Bump the version number in _pyproject.toml_ and _spacypdfreader.**init**.py_
- [ ] Format the code: `just format`
- [ ] Lint: `just lint`
- [ ] Run pytest:

  ```bash
  just test-matrix
  ```

- Test publishing to test PyPI: `just publish-test`
- [ ] Check the docs locally: `just preview-docs`

After merging the pull request:

- Docs will be automatically published by Netlify, verify deployment was successful
- [ ] Create a new release on GitHub
- [ ] Publish latest package to PyPi: `just publish`

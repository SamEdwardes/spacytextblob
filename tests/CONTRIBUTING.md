# Contiributing

spaCyTextBlob is happy to accept contributions from the community. Please review the guidelines below.

## Code formatting

Please use the [black](https://black.readthedocs.io/en/stable/) for formatting code before submitting a PR.

## Testing

Please validate that all tests pass before submitting a PR by running:

```bash
pytest
```

## Docs

To build the docs please run:

```bash
bash scripts/build_docs.sh
```

If you add new documentation using a jupyter notebook please make sure to update [scripts/build_docs.sh](scripts/build_docs.sh) to include the new notebook.


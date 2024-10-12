# Changelog

## 5.0.0 (2024-10-12)

**Breaking changes**

- Update supported Python versions from 3.9 to 3.12.
- Removed support for the `textblob-de` extension. See [#25](https://github.com/SamEdwardes/spacytextblob/issues/25) for more details.
- Removed support for accessing `._.polarity`, `._.sentiment`, `._.subjectivity`, and `._.assessments`. Now, only the `._.blob` attribute is exposed. All other textblob attributes should be access through it. For example: `._.blob.polarity`, `._.blob.sentiment`, `._.blob.subjectivity`, and `._.blob.sentiment_assessments.assessments`. This simplifies the code base and makes it easier to maintain. Lastly, this means that the config option `{"blob_only": bool}` was removed.

**Other changes**

- Use `uv` instead of `poetry`.

## 4.0.0 (2022-02-19)

- New custom attribute `doc._.blob`, `span._.blob`, `token._.blob`.
- Support for TextBlob extensions (https://textblob.readthedocs.io/en/dev/extensions.html#extensions).
- Docs are build using Material for MkDocs (https://squidfunk.github.io/mkdocs-material/) instead of Docusaurus.

## 3.0.1 (2021-05-05)

- Update the README on PyPi.

## 3.0 (2021-04-02)

- Dropped support for spaCy 2.0 API.

## 0.1.0 to 0.1.7

- Supports spaCy 2.0 API.
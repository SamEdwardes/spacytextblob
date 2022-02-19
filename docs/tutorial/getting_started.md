# Getting started

## Basic usage

When you add *spacytextblob* into your spaCy pipeline a new custom attribute is created named `._.blob`. The `._.blob` attribute is a `textblob.TextBlob` object from the textblob library. With it you can access all of the same methods and attributes in spaCy as you would be able to do in TextBlob.

Using spaCy and *spacytextblob*:

```python
{! docs/static/reference_code/spacytextblob_example.py !}
```

## Comparison to TextBlob

Using TextBlob:

```python
{! docs/static/reference_code/textblob_example.py !}
```

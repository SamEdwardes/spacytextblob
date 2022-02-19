# spacytextblob

[![PyPI version](https://badge.fury.io/py/spacytextblob.svg)](https://badge.fury.io/py/spacytextblob)
[![pytest](https://github.com/SamEdwardes/spacytextblob/actions/workflows/pytest.yml/badge.svg)](https://github.com/SamEdwardes/spacytextblob/actions/workflows/pytest.yml)
![PyPI - Downloads](https://img.shields.io/pypi/dm/spacytextblob?label=PyPi%20Downloads)
[![Netlify Status](https://api.netlify.com/api/v1/badges/e2f2caac-7239-45a2-b145-a00205c3befb/deploy-status)](https://app.netlify.com/sites/spacytextblob/deploys)

A TextBlob sentiment analysis pipeline component for spaCy. 

- [Docs](https://spacytextblob.netlify.app/)
- [GitHub](https://github.com/SamEdwardes/spacytextblob)
- [PyPi](https://pypi.org/project/spacytextblob/)
- [spaCy Universe](https://spacy.io/universe/project/spacy-textblob)

## Install

Install *spacytextblob* from PyPi.

```bash
pip install spacytextblob
```

TextBlob requires additional data to be downloaded before getting started.

```bash
python -m textblob.download_corpora
```

spaCy also requires that you download a model to get started.

```bash
python -m spacy download en_core_web_sm
```

## Quick Start

*spacytextblob* allows you to access all of the attributes created of the `textblob.TextBlob` class but within the spaCy framework. The code below will demonstrate how to use *spacytextblob* on a simple string.

```python
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load('en_core_web_sm')
text = "I had a really horrible day. It was the worst day ever! But every now and then I have a really good day that makes me happy."
nlp.add_pipe("spacytextblob")
doc = nlp(text)

print(doc._.blob.polarity)
# -0.125

print(doc._.blob.subjectivity)
# 0.9

print(doc._.blob.sentiment_assessments.assessments)
# [(['really', 'horrible'], -1.0, 1.0, None), (['worst', '!'], -1.0, 1.0, None), (['really', 'good'], 0.7, 0.6000000000000001, None), (['happy'], 0.8, 1.0, None)]
```

In comparison, here is how the same code would look using `TextBlob`:

```python
from textblob import TextBlob

text = "I had a really horrible day. It was the worst day ever! But every now and then I have a really good day that makes me happy."
blob = TextBlob(text)

print(blob.sentiment_assessments.polarity)
# -0.125

print(blob.sentiment_assessments.subjectivity)
# 0.9

print(blob.sentiment_assessments.assessments)
# [(['really', 'horrible'], -1.0, 1.0, None), (['worst', '!'], -1.0, 1.0, None), (['really', 'good'], 0.7, 0.6000000000000001, None), (['happy'], 0.8, 1.0, None)]
```

## Quick Reference

*spacytextblob* performs sentiment analysis using the [TextBlob](https://textblob.readthedocs.io/en/dev/quickstart.html) library. Adding *spacytextblob* to a spaCy nlp pipeline creates a new extension attribute for the `Doc`, `Span`, and `Token` classes from spaCy.

- `Doc._.blob`
- `Span._.blob`
- `Token._.blob`

The `._.blob` attribute contains all of the methods and attributes that belong to the `textblob.TextBlob` class Some of the common methods and attributes include: 

- **`._.blob.polarity`**: a float within the range [-1.0, 1.0].
- **`._.blob.subjectivity`**: a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective. 
- **`._.blob.sentiment_assessments.assessments`**: a list of polarity and subjectivity scores for the assessed tokens.

See the [textblob docs](https://textblob.readthedocs.io/en/dev/api_reference.html#textblob.blob.TextBlob) for the complete listing of all attributes and methods that are available in `._.blob`.

## Reference and Attribution

- TextBlob
    - [https://github.com/sloria/TextBlob](https://github.com/sloria/TextBlob)
    - [https://textblob.readthedocs.io/en/latest/](https://textblob.readthedocs.io/en/latest/)
- negspaCy (for inspiration in writing pipeline and organizing repo)
    - [https://github.com/jenojp/negspacy](https://github.com/jenojp/negspacy)
- spaCy custom components
    - [https://spacy.io/usage/processing-pipelines#custom-components](https://spacy.io/usage/processing-pipelines#custom-components)

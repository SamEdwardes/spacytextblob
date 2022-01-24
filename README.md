# spaCyTextBlob <a href='https://spacytextblob.netlify.app/'><img src='website/static/img/logo-thumb-circle-250x250.png' align="right" height="139" /></a>

[![PyPI version](https://badge.fury.io/py/spacytextblob.svg)](https://badge.fury.io/py/spacytextblob)
[![pytest](https://github.com/SamEdwardes/spaCyTextBlob/actions/workflows/pytest.yml/badge.svg)](https://github.com/SamEdwardes/spaCyTextBlob/actions/workflows/pytest.yml)
![PyPI - Downloads](https://img.shields.io/pypi/dm/spacytextblob?label=PyPi%20Downloads)
[![Netlify Status](https://api.netlify.com/api/v1/badges/e2f2caac-7239-45a2-b145-a00205c3befb/deploy-status)](https://app.netlify.com/sites/spacytextblob/deploys)


A TextBlob sentiment analysis pipeline compponent for spaCy. 

Version 3.0 is a major version update providing support for spaCy 3.0's new interface for adding pipeline components. As a result, it is not backwards compatible with previous versions of spaCyTextBlob. For compatability with spaCy 2.0 please use `pip install spacytextblob==0.1.7`.

*Note that version 1.0, and 2.0 have been skipped. The numbering has been aligned with spaCy's version numbering in the hopes of making it easier to compar.*

- [Docs](https://spacytextblob.netlify.app/)
- [GitHub](https://github.com/SamEdwardes/spaCyTextBlob)
- [PyPi](https://pypi.org/project/spacytextblob/)

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [Quick Reference](#quick-reference)
- [Reference and Attribution](#reference-and-attribution)

## Install

Install spaCyTextBlob from pypi.

```bash
pip install spacytextblob
```

TextBlob also requires some data to be downloaded before getting started.

```bash
python -m textblob.download_corpora
```

spaCy requires that you download a model to get started.

```bash
python -m spacy download en_core_web_sm
```

## Quick Start

spaCyTextBlob allows you to access all of the attributes created by TextBlob sentiment method but within the spaCy framework. The code below will demonstrate how to use spaCyTextBlob on a simple string.


```python
text = "I had a really horrible day. It was the worst day ever! But every now and then I have a really good day that makes me happy."
```

Using `spaCyTextBlob`:


```python
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe("spacytextblob")
doc = nlp(text)
```


```python
print('Polarity:', doc._.polarity)
```

    Polarity: -0.125



```python
print('Sujectivity:', doc._.subjectivity)
```

    Sujectivity: 0.9



```python
print('Assessments:', doc._.assessments)
```

    Assessments: [(['really', 'horrible'], -1.0, 1.0, None), (['worst', '!'], -1.0, 1.0, None), (['really', 'good'], 0.7, 0.6000000000000001, None), (['happy'], 0.8, 1.0, None)]


Using `TextBlob`:


```python
from textblob import TextBlob
blob = TextBlob(text)
```


```python
print(blob.sentiment_assessments.polarity)
```

    -0.125



```python
print(blob.sentiment_assessments.subjectivity)
```

    0.9



```python
print(blob.sentiment_assessments.assessments)
```

    [(['really', 'horrible'], -1.0, 1.0, None), (['worst', '!'], -1.0, 1.0, None), (['really', 'good'], 0.7, 0.6000000000000001, None), (['happy'], 0.8, 1.0, None)]


## Quick Reference

spaCyTextBlob performs sentiment analysis using the [TextBlob](https://textblob.readthedocs.io/en/dev/quickstart.html) library. Adding spaCyTextBlob to a spaCy nlp pipeline provides access to three new extension attributes.

- `._.polarity`
- `._.subjectivity`
- `._.assessments`

These extension attributes can be accessed at the `Doc`, `Span`, or `Token` level.

Polarity is a float within the range [-1.0, 1.0], subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective, and assessments is a list of polarity and subjectivity scores for the assessed tokens.

## Reference and Attribution

- TextBlob
    - [https://github.com/sloria/TextBlob](https://github.com/sloria/TextBlob)
    - [https://textblob.readthedocs.io/en/latest/](https://textblob.readthedocs.io/en/latest/)
- negspaCy (for inpiration in writing pipeline and organizing repo)
    - [https://github.com/jenojp/negspacy](https://github.com/jenojp/negspacy)
- spaCy custom components
    - [https://spacy.io/usage/processing-pipelines#custom-components](https://spacy.io/usage/processing-pipelines#custom-components)

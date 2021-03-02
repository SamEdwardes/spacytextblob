# spaCyTextBlob

A TextBlob sentiment analysis pipeline compponent for spaCy.

- [Docs](https://spacytextblob.netlify.app/)
- [GitHub](https://github.com/SamEdwardes/spaCyTextBlob)
- [PyPi](https://pypi.org/project/spacytextblob/)

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [API](#api)
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


```python
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe("spacytextblob")
text = "I had a really horrible day. It was the worst day ever! But every now and then I have a really good day that makes me happy."
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


## Reference and Attribution

- TextBlob
    - [https://github.com/sloria/TextBlob](https://github.com/sloria/TextBlob)
    - [https://textblob.readthedocs.io/en/latest/](https://textblob.readthedocs.io/en/latest/)
- negspaCy (for inpiration in writing pipeline and organizing repo)
    - [https://github.com/jenojp/negspacy](https://github.com/jenojp/negspacy)
- spaCy custom components
    - [https://spacy.io/usage/processing-pipelines#custom-components](https://spacy.io/usage/processing-pipelines#custom-components)

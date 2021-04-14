---
id: getting_started
title: Getting Started
slug: /
---
## Installation

Install spaCyTextBlob from pypi.

```bash
pip install spacytextblob
```

TextBlob requires some data to be downloaded before getting started.

```bash
python -m textblob.download_corpora
```

spaCy requires that you download a model to get started.

```bash
python -m spacy download en_core_web_sm
```

## Quickstart

First you need to add SpacyTextBlob into the spaCy pipeline. Note that as of spaCy version 3.0 the method of adding a custom pipeline component has changed.


```python
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe("spacytextblob")
print(nlp.pipe_names) 
```

    ['tok2vec', 'tagger', 'parser', 'ner', 'attribute_ruler', 'lemmatizer', 'spacytextblob']


Then you can call `nlp()` as you usually would and sentiment analysis will automtically be performed.


```python
text = "I had a really horrible day. It was the worst day ever! But every now and then I have a really good day that makes me happy."
doc = nlp(text)
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


## Comparison to `TextBlob`


```python
from textblob import TextBlob
text = "I had a really horrible day. It was the worst day ever! But every now and then I have a really good day that makes me happy."
doc = nlp(text)
blob = TextBlob(text)
```


```python
print('Polarity:', doc._.polarity, blob.sentiment.polarity)
```

    Polarity: -0.125 -0.125



```python
print('Subjectivity:', doc._.subjectivity, blob.sentiment.subjectivity)
```

    Subjectivity: 0.9 0.9



```python
print('Polarity:')
print(doc._.assessments)
print(blob.sentiment_assessments.assessments)
```

    Polarity:
    [(['really', 'horrible'], -1.0, 1.0, None), (['worst', '!'], -1.0, 1.0, None), (['really', 'good'], 0.7, 0.6000000000000001, None), (['happy'], 0.8, 1.0, None)]
    [(['really', 'horrible'], -1.0, 1.0, None), (['worst', '!'], -1.0, 1.0, None), (['really', 'good'], 0.7, 0.6000000000000001, None), (['happy'], 0.8, 1.0, None)]


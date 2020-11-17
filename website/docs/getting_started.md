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

First you need to add SpacyTextBlob to the end of the spaCy pipeline.


```python
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load('en_core_web_sm')
spacy_text_blob = SpacyTextBlob()
nlp.add_pipe(spacy_text_blob)

# pipeline contains component name
print(nlp.pipe_names) 
```

    ['tagger', 'parser', 'ner', 'text_blob_sentiment']
    

Then you can call nlp() as you usually would and sentiment analysis will be automtically performed.


```python
text = "I had a really horrible day. It was the worst day ever! But every now and then I have a really good day that makes me happy."
doc = nlp(text)
print('Polarity:', doc._.sentiment.polarity)
print('Sujectivity:', doc._.sentiment.subjectivity)
print('Assessments:', doc._.sentiment.assessments)
```

    Polarity: -0.125
    Sujectivity: 0.9
    Assessments: [(['really', 'horrible'], -1.0, 1.0, None), (['worst', '!'], -1.0, 1.0, None), (['really', 'good'], 0.7, 0.6000000000000001, None), (['happy'], 0.8, 1.0, None)]
    


```python

```

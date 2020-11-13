---
id: example
title: Examples
---
## Using on a single text


```python
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load('en_core_web_sm')
spacy_text_blob = SpacyTextBlob()
nlp.add_pipe(spacy_text_blob)

text = "I had a really horrible day. It was the worst day ever! But every now and then I have a really good day that makes me happy."
doc = nlp(text)
```

You can identify the sentiment at the doc level.


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


You can also identify sentiment at the sentence level


```python
for sentence in doc.sents:
    print('=' * 64)
    print('Polarity:', sentence._.polarity)
    print('Sujectivity:', sentence._.subjectivity)
    print('Assessments:', sentence._.assessments)
```

    ================================================================
    Polarity: -1.0
    Sujectivity: 1.0
    Assessments: [(['really', 'horrible'], -1.0, 1.0, None)]
    ================================================================
    Polarity: -1.0
    Sujectivity: 1.0
    Assessments: [(['worst', '!'], -1.0, 1.0, None)]
    ================================================================
    Polarity: 0.75
    Sujectivity: 0.8
    Assessments: [(['really', 'good'], 0.7, 0.6000000000000001, None), (['happy'], 0.8, 1.0, None)]


## Using on a multiple texts


```python
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load('en_core_web_sm')
spacy_text_blob = SpacyTextBlob()
nlp.add_pipe(spacy_text_blob)

text1 = "I had a really horrible day. It was the worst day ever! But every now and then I have a really good day that makes me happy."
text2 = "Wow I had just the best day ever today! I cannot wait to tell the world."
docs = nlp.pipe([text1, text2])
for doc in docs:
    print('=' * 64)
    print(doc.text)
    print('Polarity:', doc._.polarity)
    print('Sujectivity:', doc._.subjectivity)
    print('Assessments:', doc._.assessments)
```

    ================================================================
    I had a really horrible day. It was the worst day ever! But every now and then I have a really good day that makes me happy.
    Polarity: -0.125
    Sujectivity: 0.9
    Assessments: [(['really', 'horrible'], -1.0, 1.0, None), (['worst', '!'], -1.0, 1.0, None), (['really', 'good'], 0.7, 0.6000000000000001, None), (['happy'], 0.8, 1.0, None)]
    ================================================================
    Wow I had just the best day ever today! I cannot wait to tell the world.
    Polarity: 0.55
    Sujectivity: 0.65
    Assessments: [(['wow'], 0.1, 1.0, None), (['best', '!'], 1.0, 0.3, None)]


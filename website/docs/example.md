---
id: example
title: Examples
---
## Using on a single text


```python
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe("spacytextblob")

text = "I had a really horrible day. It was the worst day ever! But every now and then I have a really good day that makes me happy."
doc = nlp(text)
```

By adding the pipeline, the extensions  `._.polarity`, `._.subjectivity`, and `._.assessments` will be added to `Doc`, `Span`, and `Token` objects.  You can assess specific details below:
- `.polarity`: a float within the range (-1.0, 1.0)
- `.subjectivity`: a float within the range (0.0, 1.0) where 0.0 is very objective and 1.0 is very subjective
- `.assessments`: a list of polarity and subjectivity scores for the assessed tokens.


```python
print(doc._.polarity)
```

    -0.125
    


```python
print(doc._.subjectivity)
```

    0.9
    


```python
print(doc._.assessments)
```

    [(['really', 'horrible'], -1.0, 1.0, None), (['worst', '!'], -1.0, 1.0, None), (['really', 'good'], 0.7, 0.6000000000000001, None), (['happy'], 0.8, 1.0, None)]
    

You can identify the sentiment at the `Span` or `Token` level.


```python
for span in doc.sents:
    print(span.text, span._.polarity, span._.subjectivity)
```

    I had a really horrible day. -1.0 1.0
    It was the worst day ever! -1.0 1.0
    But every now and then I have a really good day that makes me happy. 0.75 0.8
    


```python
for token in doc:
    print(token.text, token._.polarity, token._.subjectivity)
```

    I 0.0 0.0
    had 0.0 0.0
    a 0.0 0.0
    really 0.2 0.2
    horrible -1.0 1.0
    day 0.0 0.0
    . 0.0 0.0
    It 0.0 0.0
    was 0.0 0.0
    the 0.0 0.0
    worst -1.0 1.0
    day 0.0 0.0
    ever 0.0 0.0
    ! 0.0 0.0
    But 0.0 0.0
    every 0.0 0.0
    now 0.0 0.0
    and 0.0 0.0
    then 0.0 0.0
    I 0.0 0.0
    have 0.0 0.0
    a 0.0 0.0
    really 0.2 0.2
    good 0.7 0.6000000000000001
    day 0.0 0.0
    that 0.0 0.0
    makes 0.0 0.0
    me 0.0 0.0
    happy 0.8 1.0
    . 0.0 0.0
    

## Using on a multiple texts


```python
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe("spacytextblob")

text1 = "I had a really horrible day. It was the worst day ever! But every now and then I have a really good day that makes me happy."
text2 = "Wow I had just the best day ever today! I cannot wait to tell the world."
docs = list(nlp.pipe([text1, text2]))
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
    

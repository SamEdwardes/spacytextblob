# spaCyTextBlob

A TextBlob sentiment analysis pipeline compponent for spaCy.

**Repo**: [https://github.com/SamEdwardes/spaCyTextBlob](https://github.com/SamEdwardes/spaCyTextBlob)<br>
**PyPi**: [https://pypi.org/project/spacytextblob/](https://pypi.org/project/spacytextblob/)

## Table of Contents

- [Install](#install)
- [Usage](#usage)
    - [How to load the package in spaCy pipeline](#how-to-load-the-package-in-spaCy-pipeline)
    - [How to use the pipeline](#how-to-use-the-pipeline)
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

## Usage

### How to load the package in spaCy pipeline


```python
import spacy
from spacytextblob.textblob import SpacyTextBlob

nlp = spacy.load('en_core_web_sm')
spacy_text_blob = SpacyTextBlob()
nlp.add_pipe(spacy_text_blob)

# pipeline contains component name
print(nlp.pipe_names) 

```

    ['tagger', 'parser', 'ner', 'spaCyTextBlob']
    

### How to use the pipeline

By adding `SpacyTextBlob` into the pipeline sentiment analysis is perofmed on the doc everytime you call `nlp`.


```python
text = "I had a really horrible day. It was the worst day ever!"
doc = nlp(text)
print('Polarity:', doc._.polarity)
print('Sujectivity:', doc._.subjectivity)
print('Assessments:', doc._.assessments)
```

    Polarity: -1.0
    Sujectivity: 1.0
    Assessments: [(['really', 'horrible'], -1.0, 1.0, None), (['worst', '!'], -1.0, 1.0, None)]
    


```python
text = "Wow I had just the best day ever today!"
doc = nlp(text)
print('Polarity:', doc._.polarity)
print('Sujectivity:', doc._.subjectivity)
print('Assessments:', doc._.assessments)
```

    Polarity: 0.55
    Sujectivity: 0.65
    Assessments: [(['wow'], 0.1, 1.0, None), (['best', '!'], 1.0, 0.3, None)]
    

## API

To make the usage simpler spacy provides custom extensions which a library can use. This makes it easier for the user to get the desired data. The below tables summaries the extensions.

### `spacy.Doc` extensions


| Extension | Type | Description | Default |
|-----------|------|-------------|---------|
| doc._.polarity | `Float` | The polarity of the document. The polarity score is a float within the range [-1.0, 1.0]. | `None` |
| doc._.sujectivity | `Float` | The subjectivity of the document. The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective. | `None` |
| doc._.assessments | `tuple` | Return a tuple of form (polarity, subjectivity, assessments ) where polarity is a float within the range [-1.0, 1.0], subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective, and assessments is a list of polarity and subjectivity scores for the assessed tokens. | `None` |




## Reference and Attribution

- TextBlob
    - [https://github.com/sloria/TextBlob](https://github.com/sloria/TextBlob)
    - [https://textblob.readthedocs.io/en/latest/](https://textblob.readthedocs.io/en/latest/)
- negspaCy (for inpiration in writing pipeline and organizing repo)
    - [https://github.com/jenojp/negspacy](https://github.com/jenojp/negspacy)
- spaCy custom components
    - [https://spacy.io/usage/processing-pipelines#custom-components](https://spacy.io/usage/processing-pipelines#custom-components)

# TextBlob Extensions

## Usage

TextBlob supports adding custom models and new languages through “extensions”. Check out the TextBlob docs ([https://textblob.readthedocs.io/en/dev/extensions.html#extensions](https://textblob.readthedocs.io/en/dev/extensions.html#extensions)) for more details.

*spacytextblob* also supports the use of TextBlob extensions. To use a TextBlob extension you need to pass some additional information to the `config` parameter when initializing the *spacytextblob* pipeline component.

```python
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
from textblob_de import TextBlobDE


text = '''
Heute ist der 3. Mai 2014 und Dr. Meier feiert seinen 43. Geburtstag. Ich muss 
unbedingt daran denken, Mehl, usw. für einen Kuchen einzukaufen. Aber leider 
habe ich nur noch EUR 3.50 in meiner Brieftasche.
'''

@spacy.registry.misc("spacytextblob.de_blob") # 1
def create_de_blob():
    return TextBlobDE

config = {
    "blob_only": True,
    "custom_blob": {"@misc": "spacytextblob.de_blob"}
}

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("spacytextblob", config=config)
doc = nlp(text)

print(doc._.blob.sentences)
# [Sentence("Heute ist der 3. Mai 2014 und Dr. Meier feiert seinen 43. Geburtstag."), Sentence("Ich muss unbedingt daran denken, Mehl, usw. für einen Kuchen einzukaufen."), Sentence("Aber leider habe ich nur noch EUR 3.50 in meiner Brieftasche.")]

print(doc._.blob.sentiment)
# Sentiment(polarity=0.0, subjectivity=0.0)

print(doc._.blob.tags)
# [('Heute', 'RB'), ('ist', 'VB'), ('der', 'DT'), ('3.', 'LS'), ('Mai', 'NN'), ('2014', 'CD'), ('und', 'CC'), ('Dr.', 'NN'), ('Meier', 'NN'), ('feiert', 'NN'), ('seinen', 'PRP$'), ('43.', 'CD'), ('Geburtstag', 'NN'), ('Ich', 'PRP'), ('muss', 'VB'), ('unbedingt', 'RB'), ('daran', 'RB'), ('denken', 'VB'), ('Mehl', 'NN'), ('usw.', 'IN'), ('für', 'IN'), ('einen', 'DT'), ('Kuchen', 'JJ'), ('einzukaufen', 'NN'), ('Aber', 'CC'), ('leider', 'VBN'), ('habe', 'VB'), ('ich', 'PRP'), ('nur', 'RB'), ('noch', 'IN'), ('EUR', 'NN'), ('3.50', 'CD'), ('in', 'IN'), ('meiner', 'JJ'), ('Brieftasche', 'NN')]

```

## Extensions

The following extensions have been tested and are supported. Other extensions may work, but have not been tested.

### textblob-de

German language support for TextBlob by Steven Loria [https://github.com/markuskiller/textblob-de](https://github.com/markuskiller/textblob-de)

```python
{! docs/static/reference_code/textblob_de_example.py !}
```

### textblob-fr

French language support for TextBlob [https://github.com/sloria/textblob-fr](https://github.com/sloria/textblob-fr).

```python
{! docs/static/reference_code/textblob_fr_example.py !}
```

### textblob-aptagger

!!! warning

    textblob-aptagger is **not** supported. As of TextBlob 0.11.0, TextBlob uses NLTK's averaged perceptron tagger by default. This package is no longer necessary.


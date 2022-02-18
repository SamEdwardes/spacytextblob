# TextBlob Extensions

## Usage

TextBlob supports adding custom models and new languages through “extensions”. Check out the TextBlob docs ([https://textblob.readthedocs.io/en/dev/extensions.html#extensions](https://textblob.readthedocs.io/en/dev/extensions.html#extensions)) for more details.

*spacytextblob* also supports the use of TextBlob extensions. To use a TextBlob extension you need to pass some additional information to the `config` parameter when initializing the *spacytextblob* pipeline component.

```python linenums="1"
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
from textblob_de import TextBlobDE # (1)


text = '''
Heute ist der 3. Mai 2014 und Dr. Meier feiert seinen 43. Geburtstag. Ich muss 
unbedingt daran denken, Mehl, usw. für einen Kuchen einzukaufen. Aber leider 
habe ich nur noch EUR 3.50 in meiner Brieftasche.
'''

@spacy.registry.misc("spacytextblob.de_blob") # (2)
def create_de_blob():
    return TextBlobDE # (3)


nlp = spacy.load("de_core_news_sm")

nlp.add_pipe(
    "spacytextblob",  # (4)
    config={ # (5)
        "blob_only": True, # (6)
        "custom_blob": {"@misc": "spacytextblob.de_blob"} # (7)
    }
)
doc = nlp(text)

print(doc._.blob.sentences)
# [Sentence("Heute ist der 3. Mai 2014 und Dr. Meier feiert seinen 43. Geburtstag."), Sentence("Ich muss unbedingt daran denken, Mehl, usw. für einen Kuchen einzukaufen."), Sentence("Aber leider habe ich nur noch EUR 3.50 in meiner Brieftasche.")]

print(doc._.blob.sentiment)
# Sentiment(polarity=0.0, subjectivity=0.0)

print(doc._.blob.tags)
# [('Heute', 'RB'), ('ist', 'VB'), ('der', 'DT'), ('3.', 'LS'), ('Mai', 'NN'), ('2014', 'CD'), ('und', 'CC'), ('Dr.', 'NN'), ('Meier', 'NN'), ('feiert', 'NN'), ('seinen', 'PRP$'), ('43.', 'CD'), ('Geburtstag', 'NN'), ('Ich', 'PRP'), ('muss', 'VB'), ('unbedingt', 'RB'), ('daran', 'RB'), ('denken', 'VB'), ('Mehl', 'NN'), ('usw.', 'IN'), ('für', 'IN'), ('einen', 'DT'), ('Kuchen', 'JJ'), ('einzukaufen', 'NN'), ('Aber', 'CC'), ('leider', 'VBN'), ('habe', 'VB'), ('ich', 'PRP'), ('nur', 'RB'), ('noch', 'IN'), ('EUR', 'NN'), ('3.50', 'CD'), ('in', 'IN'), ('meiner', 'JJ'), ('Brieftasche', 'NN')]
```

1. Load the TextBlob extension package.
2. For a function to be used inside the NLP pipeline you must register the function with spacy using `@spacy.registry.misc()`. You can name the function what ever you like. For the example I have registered the function with the name `"spacytextblob.de_blob"`.
3. *spacytextblob* is able to support TextBlob extensions by replacing the default `textblob.TextBlob` with an alternative. In the case of the [textblob-de](https://github.com/markuskiller/textblob-de) extension they provide an alternative blob that you can import (`from textblob_de import TextBlobDE`).
4. Add *spacytextblob* to your spaCy pipeline as you normally would.
5. The `config` parameter allows you to pass additional configuration options to the *spacytextblob* pipeline.
6. When using a TextBlob extension you should always set `"blob_only": True`. The extension may modify the textblob.TextBlob object. By setting `"blob_only": True` *spacytextblob* will only expose `._.blob` and not attempt to expose `._.polarity`, `._.subjectivity`, or `._.assessments`.
7. The `"custom_blob"` key should be assigned to a dictionary that tells spaCy what function to replace `textblob.TextBlob` with. In this case, we want to replace it with `TextBlobDE`. The key of the dictionary is `"@misc"`. This tells spaCy to look into the misc section of the spaCy register. The value should be the string name of the function that we registered above in line 12.

## Extensions

The following extensions have been tested and are supported. Other extensions may work, but have not been tested.

### textblob-de

textblob-de is a TextBlob extensions that enables German language support for TextBlob by Steven Loria ([https://github.com/markuskiller/textblob-de](https://github.com/markuskiller/textblob-de)). To use it with *spacytextblob* First install a spaCy model that supports German ([https://spacy.io/models/de](https://spacy.io/models/de)):

```bash
python -m spacy download de_core_news_sm
```

The code below demonstrates how you can then use and access textblob-de within *spacytextblob*.

```python linenums="1"
{! docs/static/reference_code/textblob_de_example.py !}
```

### textblob-fr

textblob-fr is a TextBlob extension that enables French language support for TextBlob ([https://github.com/sloria/textblob-fr](https://github.com/sloria/textblob-fr)). To use it with *spacytextblob* First install a spaCy model that supports French ([https://spacy.io/models/fr](https://spacy.io/models/fr)):

```bash
python -m spacy download fr_core_news_sm
```

The code below demonstrates how you can then use and access textblob-fr within *spacytextblob*.

```python linenums="1"
{! docs/static/reference_code/textblob_fr_example.py !}
```

### textblob-aptagger

!!! warning

    textblob-aptagger is **not** supported. As of TextBlob 0.11.0, TextBlob uses NLTK's averaged perceptron tagger by default. This package is no longer necessary ([https://github.com/sloria/textblob-aptagger](https://github.com/sloria/textblob-aptagger)).


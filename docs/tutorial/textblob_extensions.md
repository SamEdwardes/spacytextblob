# TextBlob Extensions

## Usage

TextBlob supports adding custom models and new languages through “extensions”. Check out the TextBlob docs ([https://textblob.readthedocs.io/en/dev/extensions.html#extensions](https://textblob.readthedocs.io/en/dev/extensions.html#extensions)) for more details.

*spacytextblob* also supports the use of TextBlob extensions. To use a TextBlob extension you need to pass some additional information to the `config` parameter when initializing the *spacytextblob* pipeline component.

```python linenums="1"
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer # (1)

text = u"Quelle belle matinée"

@spacy.registry.misc("spacytextblob.fr_blob") # (2)
def create_fr_blob():
    tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    return tb # (3)

nlp_fr = spacy.load("fr_core_news_sm")

nlp_fr.add_pipe(
    "spacytextblob", # (4)
    config={ # (5)
        "custom_blob": {"@misc": "spacytextblob.fr_blob"} # (6)
    }
)

doc = nlp_fr(text)

print(doc)
# Quelle belle matinée
print(doc._.blob)
# Quelle belle matinée
print(doc._.blob.sentiment)
# (0.8, 0.8)
```

1. Load the TextBlob extension package.
2. For a function to be used inside the NLP pipeline you must register the function with spacy using `@spacy.registry.misc()`. You can name the function what ever you like. For the example I have registered the function with the name `"spacytextblob.fr_blob"`.
3. *spacytextblob* is able to support TextBlob extensions by replacing the default `textblob.TextBlob` with an alternative.
4. Add *spacytextblob* to your spaCy pipeline as you normally would.
5. The `config` parameter allows you to pass additional configuration options to the *spacytextblob* pipeline.
6. The `"custom_blob"` key should be assigned to a dictionary that tells spaCy what function to replace `textblob.TextBlob` with. In this case, we want to replace it with `TextBlobDE`. The key of the dictionary is `"@misc"`. This tells spaCy to look into the misc section of the spaCy register. The value should be the string name of the function that we registered above in line 12.

## Extensions

The following extensions have been tested and are supported. Other extensions may work, but have not been tested.

### textblob-fr

textblob-fr is a TextBlob extension that enables French language support for TextBlob ([https://github.com/sloria/textblob-fr](https://github.com/sloria/textblob-fr)).

```bash
pip install textblob-fr
```

To use it with *spacytextblob* First install a spaCy model that supports French ([https://spacy.io/models/fr](https://spacy.io/models/fr)):

```bash
python -m spacy download fr_core_news_sm
```

The code below demonstrates how you can then use and access textblob-fr within *spacytextblob*.

```python linenums="1"
{! docs/static/reference_code/textblob_fr_example.py !}
```

### textblob-de

!!! warning

    textblob-de is **not** supported. As of spacytextblob 4.1.0. The textblob-de library depends on a Google Translate feature that no longer works. More details can be found in this issue [https://github.com/markuskiller/textblob-de/issues/24](https://github.com/markuskiller/textblob-de/issues/24).

### textblob-aptagger

!!! warning

    textblob-aptagger is **not** supported. As of TextBlob 0.11.0, TextBlob uses NLTK's averaged perceptron tagger by default. This package is no longer necessary ([https://github.com/sloria/textblob-aptagger](https://github.com/sloria/textblob-aptagger)).

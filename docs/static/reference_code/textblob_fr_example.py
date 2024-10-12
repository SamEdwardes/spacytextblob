import spacy
from textblob import Blobber
from textblob_fr import PatternAnalyzer, PatternTagger

from spacytextblob.spacytextblob import SpacyTextBlob  # noqa: F401


@spacy.registry.misc("spacytextblob.fr_blob")
def create_fr_blob():
    tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    return tb


config = {"custom_blob": {"@misc": "spacytextblob.fr_blob"}}

nlp_fr = spacy.load("fr_core_news_sm")
nlp_fr.add_pipe("spacytextblob", config=config)
text = "Quelle belle matinée"
doc = nlp_fr(text)

print(doc)
# Quelle belle matinée
print(doc._.blob)
# Quelle belle matinée
print(doc._.blob.sentiment)
# (0.8, 0.8)

import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer

@spacy.registry.misc("spacytextblob.fr_blob")
def create_fr_blob():
    tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    return tb

config = {
    "blob_only": True,
    "custom_blob": {"@misc": "spacytextblob.fr_blob"}
}

nlp_fr = spacy.load("en_core_web_sm")
nlp_fr.add_pipe("spacytextblob", config=config)
text = u"Quelle belle matinée"
doc = nlp_fr(text)

print(doc)
print(doc._.blob)
print(doc._.blob.sentiment)
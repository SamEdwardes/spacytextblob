import spacy
from rich import inspect, print
from textblob_fr import PatternAnalyzer, PatternTagger

from spacytextblob.spacytextblob import SpacyTextBlob


@spacy.registry.misc("acronyms.slang_dict.v1")
def create_acronyms_slang_dict():
    dictionary = {"lol": "laughing out loud", "brb": "be right back"}
    dictionary.update({value: key for key, value in dictionary.items()})
    return dictionary

@spacy.registry.misc("spacytextblob.pos_tagger")
def create_pos_tagger():
    return PatternTagger()


@spacy.registry.misc("spacytextblob.analyzer")
def create_analyzer():
    return PatternAnalyzer()


nlp_fr = spacy.load("en_core_web_sm")


config = {
    "blob_only": True,
    "pos_tagger": {"@misc": "spacytextblob.pos_tagger"}, 
    "analyzer":   {"@misc": "spacytextblob.analyzer"},
}

text = u"Quelle belle matinée"
nlp_fr.add_pipe("spacytextblob", config=config)
doc = nlp_fr(text)

print(doc._.blob.sentiment)
print(doc._.blob.sentiment == (0.8, 0.8))

import spacy
from textblob_de import TextBlobDE

from spacytextblob.spacytextblob import SpacyTextBlob  # noqa: F401

text = """
Heute ist der 3. Mai 2014 und Dr. Meier feiert seinen 43. Geburtstag. Ich muss
unbedingt daran denken, Mehl, usw. für einen Kuchen einzukaufen. Aber leider
habe ich nur noch EUR 3.50 in meiner Brieftasche.
"""


@spacy.registry.misc("spacytextblob.de_blob")
def create_de_blob():
    return TextBlobDE


config = {"custom_blob": {"@misc": "spacytextblob.de_blob"}}

nlp = spacy.load("de_core_news_sm")
nlp.add_pipe("spacytextblob", config=config)
doc = nlp(text)

print(doc._.blob.sentences)
# [Sentence("Heute ist der 3. Mai 2014 und Dr. Meier feiert seinen 43. Geburtstag."), Sentence("Ich muss unbedingt daran denken, Mehl, usw. für einen Kuchen einzukaufen."), Sentence("Aber leider habe ich nur noch EUR 3.50 in meiner Brieftasche.")]

print(doc._.blob.sentiment)
# Sentiment(polarity=0.0, subjectivity=0.0)

print(doc._.blob.tags)
# [('Heute', 'RB'), ('ist', 'VB'), ('der', 'DT'), ('3.', 'LS'), ('Mai', 'NN'), ('2014', 'CD'), ('und', 'CC'), ('Dr.', 'NN'), ('Meier', 'NN'), ('feiert', 'NN'), ('seinen', 'PRP$'), ('43.', 'CD'), ('Geburtstag', 'NN'), ('Ich', 'PRP'), ('muss', 'VB'), ('unbedingt', 'RB'), ('daran', 'RB'), ('denken', 'VB'), ('Mehl', 'NN'), ('usw.', 'IN'), ('für', 'IN'), ('einen', 'DT'), ('Kuchen', 'JJ'), ('einzukaufen', 'NN'), ('Aber', 'CC'), ('leider', 'VBN'), ('habe', 'VB'), ('ich', 'PRP'), ('nur', 'RB'), ('noch', 'IN'), ('EUR', 'NN'), ('3.50', 'CD'), ('in', 'IN'), ('meiner', 'JJ'), ('Brieftasche', 'NN')]

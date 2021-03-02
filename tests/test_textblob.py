import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("spacytextblob")


def test_sentiment():
    text = "I had a really horrible day. It was the worst day ever!"
    doc = nlp(text)
    assert doc._.polarity < 0
    assert type(doc._.subjectivity) is float
    assert type(doc._.assessments) is list

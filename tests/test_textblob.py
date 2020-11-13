import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load("en_core_web_sm")
spacy_text_blob = SpacyTextBlob()
nlp.add_pipe(spacy_text_blob)


def test_pipeline_component():
    assert nlp.pipe_names[-1] == "spaCyTextBlob"


def test_sentiment():
    text = "I had a really horrible day. It was the worst day ever!"
    doc = nlp(text)
    assert doc._.polarity < 0
    assert type(doc._.subjectivity) is float
    assert type(doc._.assessments) is list

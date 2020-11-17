import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load("en_core_web_sm")
spacy_text_blob = SpacyTextBlob()
nlp.add_pipe(spacy_text_blob)


def test_pipeline_component():
    assert nlp.pipe_names[-1] == "text_blob_sentiment"


def test_negative_sentiment():
    text = "I had a really horrible day. It was the worst day ever!"
    doc = nlp(text)
    assert doc._.sentiment.polarity < 0
    assert type(doc._.sentiment.subjectivity) is float
    assert type(doc._.sentiment.assessments) is list


def test_positive_sentiment():
    text = "I had a really amazing day. It was the best day ever!"
    doc = nlp(text)
    assert doc._.sentiment.polarity > 0
    assert type(doc._.sentiment.subjectivity) is float
    assert type(doc._.sentiment.assessments) is list

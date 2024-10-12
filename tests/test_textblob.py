import pytest
import spacy
from textblob import TextBlob
from textblob.download_corpora import download_all

import spacytextblob
from spacytextblob.spacytextblob import SpacyTextBlob  # noqa: F401

# Set up textblob
download_all()


# Setup spacy
def get_nlp() -> spacy.language.Language:
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("spacytextblob")
    return nlp


def test_version():
    assert spacytextblob.__version__ == "5.0.0"


def test_types():
    nlp = get_nlp()
    text = "I had a really horrible day. It was the worst day ever!"
    doc = nlp(text)

    # Check types
    assert isinstance(doc._.blob.polarity, float)
    assert isinstance(doc._.blob.subjectivity, float)
    assert isinstance(doc._.blob.sentiment_assessments.assessments, list)
    assert isinstance(doc._.blob, TextBlob)


def test_blob_only_false_error():
    nlp_custom_config = spacy.load("en_core_web_sm")
    with pytest.raises(ValueError):
        nlp_custom_config.add_pipe("spacytextblob", config={"blob_only": False})


def test_negative_sentiment():
    nlp = get_nlp()
    text = "I had a really horrible day. It was the worst day ever!"
    doc = nlp(text)
    # Check polarity
    assert doc._.blob.polarity == -1.0
    assert doc[4]._.blob.polarity == -1.0
    assert [span._.blob.polarity for span in doc.sents] == [-1.0, -1.0]
    # Check subjectivity
    assert doc._.blob.subjectivity == 1.0
    assert doc[4]._.blob.subjectivity == 1.0
    assert [span._.blob.subjectivity for span in doc.sents] == [1.0, 1.0]


def test_positive_sentiment():
    nlp = get_nlp()
    text = "I had a really amazing day. It was the best day ever!"
    doc = nlp(text)
    # Check polarity
    assert doc._.blob.polarity == 0.8
    assert round(doc[4]._.blob.polarity, 1) == 0.6
    assert [round(span._.blob.polarity, 1) for span in doc.sents] == [0.6, 1.0]
    # Check polarity
    assert doc._.blob.subjectivity == 0.6
    assert doc[4]._.blob.subjectivity == 0.9
    assert [span._.blob.subjectivity for span in doc.sents] == [0.9, 0.3]


def test_compare_to_text_blob_example_1():
    nlp = get_nlp()
    text = "It is a very fun thing how happy puppies can make you."
    blob = TextBlob(text)
    doc = nlp(text)
    assert blob.polarity == doc._.blob.polarity
    assert blob.subjectivity == doc._.blob.subjectivity
    assert blob.sentiment_assessments[2] == doc._.blob.sentiment_assessments.assessments


def test_compare_to_text_blob_example_2():
    nlp = get_nlp()
    text = "My favourite food is Italian food. I love it."
    blob = TextBlob(text)
    doc = nlp(text)
    assert blob.polarity == doc._.blob.polarity
    assert blob.subjectivity == doc._.blob.subjectivity
    assert blob.sentiment_assessments[2] == doc._.blob.sentiment_assessments.assessments


def test_textblob_fr():
    from textblob import Blobber
    from textblob_fr import PatternAnalyzer, PatternTagger

    text = "Quelle belle matinée"
    tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    blob = tb(text)
    assert blob.sentiment == (0.8, 0.8)


def test_spacytextblob_fr():
    from textblob import Blobber
    from textblob_fr import PatternAnalyzer, PatternTagger

    @spacy.registry.misc("spacytextblob.fr_blob")
    def create_fr_blob():
        tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
        return tb

    config = {"custom_blob": {"@misc": "spacytextblob.fr_blob"}}

    nlp_fr = spacy.load("en_core_web_sm")
    nlp_fr.add_pipe("spacytextblob", config=config)
    text = "Quelle belle matinée"
    doc = nlp_fr(text)
    assert doc._.blob.sentiment == (0.8, 0.8)

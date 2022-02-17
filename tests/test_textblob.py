from numpy import isin
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
from textblob import TextBlob

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("spacytextblob")


def test_types():
    text = "I had a really horrible day. It was the worst day ever!"
    doc = nlp(text)
    
    # Check types
    assert isinstance(doc._.polarity, float)
    assert isinstance(doc._.subjectivity, float)
    assert isinstance(doc._.assessments, list)
    assert isinstance(doc._.blob, TextBlob)


def test_negative_sentiment():
    text = "I had a really horrible day. It was the worst day ever!"
    doc = nlp(text)
    # Check polarity
    assert doc._.polarity == -1.0
    assert doc[4]._.polarity == -1.0
    [span._.polarity for span in doc.sents] == [-1.0 , -1.0]
    # Check polarity
    assert doc._.subjectivity == 1.0
    assert doc[4]._.subjectivity == 1.0
    assert [span._.subjectivity for span in doc.sents] == [1.0 , 1.0]
    
    
def test_positive_sentiment():
    text = "I had a really amazing day. It was the best day ever!"
    doc = nlp(text)
    # Check polarity
    assert doc._.polarity == 0.8
    assert round(doc[4]._.polarity, 1) == 0.6
    [round(span._.polarity, 1) for span in doc.sents] == [0.6 , 1.0]
    # Check polarity
    assert doc._.subjectivity == 0.6
    assert doc[4]._.subjectivity == 0.9
    assert [span._.subjectivity for span in doc.sents] == [0.9 , 0.3]
    
    
def test_compare_to_text_blob():
    # Text example 1
    text = "It is a very fun thing how happy puppies can make you."
    blob = TextBlob(text)
    doc = nlp(text)
    assert blob.polarity == doc._.polarity
    assert blob.subjectivity == doc._.subjectivity
    assert blob.sentiment_assessments[2] == doc._.assessments
    
    # Text example 2
    text = "My favourite food is Italian food. I love it."
    blob = TextBlob(text)
    doc = nlp(text)
    assert blob.polarity == doc._.polarity
    assert blob.subjectivity == doc._.subjectivity
    assert blob.sentiment_assessments[2] == doc._.assessments

    
def test_textblob_fr():
    from textblob import Blobber
    from textblob_fr import PatternTagger, PatternAnalyzer

    text = u"Quelle belle matinée"
    tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    blob = tb(text)
    assert blob.sentiment == (0.8, 0.8)


def test_spacytextblob_fr():
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
    assert doc._.blob.sentiment == (0.8, 0.8)
    
    
def test_textblob_de():
    from textblob_de import TextBlobDE
    from textblob import Sentence
    text = '''Heute ist der 3. Mai 2014 und Dr. Meier feiert seinen 43. Geburtstag. Ich muss unbedingt daran denken, Mehl, usw. für einen Kuchen einzukaufen. Aber leider habe ich nur noch EUR 3.50 in meiner Brieftasche.'''
    blob = TextBlobDE(text)
    sentences = [
        Sentence("Heute ist der 3. Mai 2014 und Dr. Meier feiert seinen 43. Geburtstag."),
        Sentence("Ich muss unbedingt daran denken, Mehl, usw. für einen Kuchen einzukaufen."),
        Sentence("Aber leider habe ich nur noch EUR 3.50 in meiner Brieftasche.")
    ]
    assert blob.sentences == sentences


def test_spacytextblob_de():
    from textblob_de import TextBlobDE
    from textblob import Sentence
    text = '''Heute ist der 3. Mai 2014 und Dr. Meier feiert seinen 43. Geburtstag. Ich muss unbedingt daran denken, Mehl, usw. für einen Kuchen einzukaufen. Aber leider habe ich nur noch EUR 3.50 in meiner Brieftasche.'''
    
    @spacy.registry.misc("spacytextblob.de_blob")
    def create_de_blob():
        return TextBlobDE
    
    config = {
        "blob_only": True,
        "custom_blob": {"@misc": "spacytextblob.de_blob"}
    }
    
    nlp_de = spacy.load("en_core_web_sm")
    nlp_de.add_pipe("spacytextblob", config=config)
    doc = nlp_de(text)
    
    sentences = [
        Sentence("Heute ist der 3. Mai 2014 und Dr. Meier feiert seinen 43. Geburtstag."),
        Sentence("Ich muss unbedingt daran denken, Mehl, usw. für einen Kuchen einzukaufen."),
        Sentence("Aber leider habe ich nur noch EUR 3.50 in meiner Brieftasche.")
    ]
    assert doc._.blob.sentences == sentences

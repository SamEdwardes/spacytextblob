from spacy.tokens import Doc, Span, Token
from spacy.language import Language

from textblob import TextBlob


@Language.factory("spacytextblob")
class SpacyTextBlob(object):
    """A spacy pipeline object for sentiment analysis."""
    
    def __init__(self, nlp, name):
        # Register custom extensions
        if not Doc.has_extension("polarity"):            
            Doc.set_extension("polarity", default=None)
            Doc.set_extension("subjectivity", default=None)
            Doc.set_extension("assessments", default=None)
            Span.set_extension("polarity", getter=self.get_polarity)
            Span.set_extension("subjectivity", getter=self.get_subjectivity)
            Span.set_extension("assessments", getter=self.get_assessments)
            Token.set_extension("polarity", getter=self.get_polarity)
            Token.set_extension("subjectivity", getter=self.get_subjectivity)
            Token.set_extension("assessments", getter=self.get_assessments)

    def __call__(self, doc):
        # sentiment at the doc level
        sentiment = self.get_sentiment(doc)
        doc._.set("polarity", sentiment.polarity)
        doc._.set("subjectivity", sentiment.subjectivity)
        doc._.set("assessments", sentiment.assessments)
        
        return doc
            
    def get_sentiment(self, doc):
        blob = TextBlob(doc.text)
        sentiment = blob.sentiment_assessments
        return sentiment
    
    def get_polarity(self, doc):
        return self.get_sentiment(doc).polarity
    
    def get_subjectivity(self, doc):
        return self.get_sentiment(doc).subjectivity
    
    def get_assessments(self, doc):
        return self.get_sentiment(doc).assessments
    

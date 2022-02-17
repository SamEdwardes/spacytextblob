from typing import Optional, Callable, Any
from spacy.tokens import Doc, Span, Token
from spacy.language import Language

from rich import inspect, print

from textblob import TextBlob


@Language.factory("spacytextblob", default_config={"blob_only": False, "pos_tagger": None, "analyzer": None})
def create_spacytextblob_component(
    nlp: Language, 
    name: str, 
    blob_only: bool, 
    pos_tagger: Optional[Any], 
    analyzer: Optional[Any]
):
    return SpacyTextBlob(nlp, blob_only, pos_tagger, analyzer)


class SpacyTextBlob(object):
    """A spacy pipeline object for sentiment analysis."""
    
    def __init__(
        self, 
        nlp: Language, 
        blob_only: bool = False, 
        pos_tagger: Optional[Any] = None, 
        analyzer: Optional[Any] = None
    ):
        # Register custom extensions
        print(f"{pos_tagger=}")
        print(f"{analyzer=}")
        extensions = ["blob", "polarity", "subjectivity", "assessments"]
        getters = [self.get_blob, self.get_polarity, self.get_subjectivity, self.get_assessments]
        
        for ext, get in zip(extensions, getters):
            if not Doc.has_extension(ext):
                Doc.set_extension(ext, default=None)
            if not Span.has_extension(ext):
                Span.set_extension(ext, getter=get)
            if not Token.has_extension(ext):
                Token.set_extension(ext, getter=get)

        # Set class attributes
        self.blob_only = blob_only
        self.pos_tagger = pos_tagger
        self.analyzer = analyzer

    def __call__(self, doc):
        # Sentiment at the doc level
        blob = self.get_blob(doc)
        doc._.set("blob", blob)
        if self.blob_only == False:
            doc._.set("polarity", blob.sentiment.polarity)
            doc._.set("subjectivity", blob.sentiment.subjectivity)
            doc._.set("assessments", blob.sentiment_assessments.assessments)
        
        return doc
    
    def create_blob(self, doc):
        kwargs = {
            "pos_tagger": self.pos_tagger, 
            "analyzer": self.analyzer
        }
        
        print(kwargs)
        
        # Only keeps the kwargs that are note note.
        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        blob = TextBlob(doc.text, **kwargs)
        return blob
    
    def get_blob(self, doc):
        return self.create_blob(doc)
    
    def get_polarity(self, doc):
        return self.create_blob(doc).polarity
    
    def get_subjectivity(self, doc):
        return self.create_blob(doc).subjectivity
    
    def get_assessments(self, doc):
        return self.create_blob(doc).sentiment_assessments.assessments
    


from spacy.tokens import Doc, Span, Token
from textblob import TextBlob


class SpacyTextBlob(object):
    """spaCy pipeline component for adding TextBlob sentiment analysis."""

    name = "text_blob_sentiment"

    def __init__(self):
        Token.set_extension("sentiment", getter=self.get_sentiment, force=True)
        Span.set_extension("sentiment", getter=self.get_sentiment, force=True)
        Doc.set_extension("sentiment", getter=self.get_sentiment, force=True)

    def __call__(self, doc):
        return doc

    def get_sentiment(self, tokens):
        blob = TextBlob(tokens.text)
        sentiment = blob.sentiment_assessments
        return sentiment

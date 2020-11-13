from spacy.tokens import Doc, Span

from textblob import TextBlob


class SpacyTextBlob(object):
    """A spacy pipeline object for sentiment analysis."""
    name = "spaCyTextBlob"

    def __init__(self):
        Doc.set_extension("polarity", default=None, force=True)
        Doc.set_extension("subjectivity", default=None, force=True)
        Doc.set_extension("assessments", default=None, force=True)
        Span.set_extension("polarity", default=None, force=True)
        Span.set_extension("subjectivity", default=None, force=True)
        Span.set_extension("assessments", default=None, force=True)

    def __call__(self, doc):
        # sentiment at the doc level
        blob = TextBlob(doc.text)
        sentiment = blob.sentiment_assessments
        doc._.set("polarity", sentiment.polarity)
        doc._.set("subjectivity", sentiment.subjectivity)
        doc._.set("assessments", sentiment.assessments)

        # sentiment on the sentence level
        for span in doc.sents:
            blob = TextBlob(span.text)
            sentiment = blob.sentiment_assessments
            span._.set("polarity", sentiment.polarity)
            span._.set("subjectivity", sentiment.subjectivity)
            span._.set("assessments", sentiment.assessments)

        return doc

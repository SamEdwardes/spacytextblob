from spacy.tokens import Doc
from textblob import TextBlob


class SpacyTextBlob(object):
    name = "spaCyTextBlob"

    def __init__(self):
        Doc.set_extension("polarity", default=None)
        Doc.set_extension("subjectivity", default=None)
        Doc.set_extension("assessments", default=None)

    def __call__(self, doc):

        blob = TextBlob(doc.text)
        sentiment = blob.sentiment_assessments
        doc._.set("polarity", sentiment.polarity)
        doc._.set("subjectivity", sentiment.subjectivity)
        doc._.set("assessments", sentiment.assessments)
        return doc
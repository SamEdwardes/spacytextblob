import warnings
from typing import Any, Optional

from spacy.language import Language
from spacy.tokens import Doc, Span, Token
from textblob import TextBlob


@Language.factory(
    "spacytextblob", default_config={"blob_only": False, "custom_blob": None}
)
def create_spacytextblob_component(
    nlp: Language,
    name: str,
    blob_only: bool,
    custom_blob: Optional[Any],
):
    return SpacyTextBlob(nlp, blob_only, custom_blob)


class SpacyTextBlob(object):
    """A spacy pipeline object for sentiment analysis."""

    def __init__(
        self, nlp: Language, blob_only: bool = False, custom_blob: Optional[Any] = None
    ):
        # Register custom extensions
        extensions = ["blob", "polarity", "subjectivity", "assessments"]
        getters = [
            self.get_blob,
            self.get_polarity,
            self.get_subjectivity,
            self.get_assessments,
        ]

        for ext, get in zip(extensions, getters):
            if not Doc.has_extension(ext):
                Doc.set_extension(ext, default=None)
            if not Span.has_extension(ext):
                Span.set_extension(ext, getter=get)
            if not Token.has_extension(ext):
                Token.set_extension(ext, getter=get)

        # Set class attributes
        self.blob_only = blob_only
        self.custom_blob = custom_blob

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
        if self.custom_blob:
            tb = self.custom_blob
        else:
            tb = TextBlob

        blob = tb(doc.text)
        return blob

    def get_blob(self, doc):
        return self.create_blob(doc)

    def get_polarity(self, doc):
        warnings.warn(
            "`doc._.polarity` will be deprecated in future versions. Instead you should use `doc._.blob.polarity`.",
            DeprecationWarning,
        )
        return self.create_blob(doc).polarity

    def get_subjectivity(self, doc):
        warnings.warn(
            "`doc._.subjectivity` will be deprecated in future versions. Instead you should use `doc._.blob.subjectivity`.",
            DeprecationWarning,
        )
        return self.create_blob(doc).subjectivity

    def get_assessments(self, doc):
        warnings.warn(
            "`doc._.assessments` will be deprecated in future versions. Instead you should use `doc._.blob.sentiment_assessments.assessments`.",
            DeprecationWarning,
        )
        return self.create_blob(doc).sentiment_assessments.assessments

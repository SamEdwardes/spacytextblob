from typing import Any, Optional

from spacy.language import Language
from spacy.tokens import Doc, Span, Token
from textblob import TextBlob


@Language.factory("spacytextblob", default_config={"custom_blob": None})
def create_spacytextblob_component(
    nlp: Language,
    name: str,
    custom_blob: Optional[Any],
):
    return SpacyTextBlob(nlp, custom_blob)


class SpacyTextBlob(object):
    """A spacy pipeline object for sentiment analysis."""

    def __init__(self, nlp: Language, custom_blob: Optional[Any] = None):
        # Register custom extensions
        extensions = ["blob"]
        getters = [self.get_blob]

        for ext, get in zip(extensions, getters):
            if not Doc.has_extension(ext):
                Doc.set_extension(ext, default=None)
            if not Span.has_extension(ext):
                Span.set_extension(ext, getter=get)
            if not Token.has_extension(ext):
                Token.set_extension(ext, getter=get)

        # Set class attributes
        self.custom_blob = custom_blob

    def __call__(self, doc):
        # Sentiment at the doc level
        blob = self.get_blob(doc)
        doc._.set("blob", blob)
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

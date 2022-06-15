import warnings
from typing import Any, Optional

from spacy.language import Language
from spacy.tokens import Doc, Span, Token
from textblob import TextBlob


@Language.factory(
    "spacytextblob", 
    default_config={
        "blob_only": False, 
        "custom_blob": None,
        "enable_multi_process": False,
    }
)
def create_spacytextblob(
    nlp: Language,
    name: str,
    blob_only: bool = False, 
    enable_multi_process: bool = False,
    custom_blob: Optional[Any] = None,
):
    return choose_correct_class(
        nlp=nlp, 
        blob_only=blob_only, 
        custom_blob=custom_blob, 
        enable_multi_process=enable_multi_process
    )


def choose_correct_class(
    nlp: Language,
    blob_only: bool = False, 
    custom_blob: Optional[Any] = None,
    enable_multi_process: bool = False
):
    # Scenario (1): Multiprocessing:
    if enable_multi_process == True:
        if custom_blob is not None:
            raise ValueError("When `enable_multi_process` is `True` you are not able to pass in a custom blob. `custom_blob` must be `None`.")
        return SpacyTextBlobMultiProcess(nlp=nlp)
    
    # Scenario (2): TextBlob Extension or blob only:
    if custom_blob is not None or blob_only is True:
        if enable_multi_process == True:
            raise ValueError("When you are using a TextBlob extension or have selected `blob_only=True` it is not possible to do multiprocessing. Please set `enable_multi_process=False`.")
        return SpacyTextBlobExtension(nlp=nlp, custom_blob=custom_blob)

    # Scenario (3):
    return SpacyTextBlobBase(nlp=nlp)



class SpacyTextBlob(object):
    def __init__(self) -> None:
        pass

# class SpacyTextBlob(object):
     
#      def __init__(
#         self,
#         nlp: Language,
#         blob_only: bool = False, 
#         custom_blob: Optional[Any] = None,
#         enable_multi_process: bool = False
#      ):
#         return choose_correct_class(
#             nlp=nlp, 
#             blob_only=blob_only, 
#             custom_blob=custom_blob, 
#             enable_multi_process=enable_multi_process
#         )
         
    
   


class SpacyTextBlobBase(object):
    """A spacy pipeline object for sentiment analysis."""

    def __init__(self, nlp: Language):        
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

    def __call__(self, doc):
        # Sentiment at the doc level
        blob = self.get_blob(doc)
        doc._.set("blob", blob)
        doc._.set("polarity", blob.sentiment.polarity)
        doc._.set("subjectivity", blob.sentiment.subjectivity)
        doc._.set("assessments", blob.sentiment_assessments.assessments)
        return doc

    def create_blob(self, doc):
        tb = TextBlob
        blob = tb(doc.text)
        return blob

    def get_blob(self, doc):
        return self.create_blob(doc)

    def get_polarity(self, doc):
        return self.create_blob(doc).polarity

    def get_subjectivity(self, doc):
        return self.create_blob(doc).subjectivity

    def get_assessments(self, doc):
        return self.create_blob(doc).sentiment_assessments.assessments


# @Language.factory("spacytextblob_multi_process")
# def create_spacytextblob_multi_process(nlp: Language, name: str):
#     return SpacyTextBlobMultiProcess(nlp)


class SpacyTextBlobMultiProcess(object):
    """A spacy pipeline object for sentiment analysis."""

    def __init__(self, nlp: Language,):
        # Register custom extensions
        extensions = ["polarity", "subjectivity", "assessments"]
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

    def __call__(self, doc):
        blob = self.get_blob(doc)
        doc._.set("polarity", blob.sentiment.polarity)
        doc._.set("subjectivity", blob.sentiment.subjectivity)
        doc._.set("assessments", blob.sentiment_assessments.assessments)
        return doc

    def create_blob(self, doc):
        tb = TextBlob
        blob = tb(doc.text)
        return blob

    def get_blob(self, doc):
        return self.create_blob(doc)

    def get_polarity(self, doc):
        return self.create_blob(doc).polarity

    def get_subjectivity(self, doc):
        return self.create_blob(doc).subjectivity

    def get_assessments(self, doc):
        return self.create_blob(doc).sentiment_assessments.assessments


@Language.factory("spacytextblob_extension", default_config={"custom_blob": None})
def create_spacytextblob_extension_component(
    nlp: Language,
    name: str,
    custom_blob: Optional[Any],
):
    return SpacyTextBlobExtension(nlp, custom_blob)


class SpacyTextBlobExtension(object):
    """A spacy pipeline object for sentiment analysis."""

    def __init__(self, nlp: Language, custom_blob: Any):
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
        tb = self.custom_blob
        blob = tb(doc.text)
        return blob

    def get_blob(self, doc):
        return self.create_blob(doc)

from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
text = u"Quelle belle matinée"
tagger = PatternTagger()
analyzer = PatternAnalyzer()
blob = TextBlob(text, pos_tagger=tagger, analyzer=analyzer)
print(blob.sentiment)

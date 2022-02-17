# API Reference

## Config


## Custom attributes

When you add *spacytextblob* into your spaCy pipeline it exposes a custom attribute `._.blob`. This attribute is available for for the `Doc`, `Span`, and `Token` classes from spaCy.

- `Doc._.blob`
- `Span._.blob`
- `Token._.blob`

The section below outlines commonly accessed `._.blob` attributes and methods. See the [textblob docs](https://textblob.readthedocs.io/en/dev/api_reference.html#textblob.blob.TextBlob) for the complete listing of all attributes and methods that are available in `._.blob`.

### Attributes

| Name | Type | Description |
|------|------|-------------|
| `doc._.blob.polarity` | `Float` | The polarity of the document. The polarity score is a float within the range [-1.0, 1.0]. |
| `doc._.blob.subjectivity` | `Float` | The subjectivity of the document. The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective. |
| `doc._.blob.sentiment_assessments.assessments` | `tuple` | Return a tuple of form (polarity, subjectivity, assessments ) where polarity is a float within the range [-1.0, 1.0], subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective, and assessments is a list of polarity and subjectivity scores for the assessed tokens. |

### Methods

#### `doc._.blob.ngrams(n=3)`

| Name | Type | Description |
|------|------|-------------|
| n | `int` | The number of words to include in the ngram. By default `3`. |
| RETURNS | `List[WordLists]` | |



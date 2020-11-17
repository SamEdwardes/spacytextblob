---
id: api
title: API Reference
---
To make the usage simpler spacy provides custom extensions which a library can use. This makes it easier for the user to get the desired data. The below tables summaries the extensions.

## `spacy.Doc` extensions


| Extension | Type | Description |
|-----------|------|-------------|
| doc._.sentiment | `tuple` | Just like in the textblob library, sentiment returns a named tuple: (0) `.polarity`: a float within the range (-1.0, 1.0), (1) `.subjectivity`: a float within the range (0.0, 1.0) where 0.0 is very objective and 1.0 is very subjective, and (2) `.assessments`: a list of polarity and subjectivity scores for the assessed tokens.The polarity of the document. |


## `spacy.Span` extensions


| Extension | Type | Description |
|-----------|------|-------------|
| doc._.sentiment | `tuple` | Just like in the textblob library, sentiment returns a named tuple: (0) `.polarity`: a float within the range (-1.0, 1.0), (1) `.subjectivity`: a float within the range (0.0, 1.0) where 0.0 is very objective and 1.0 is very subjective, and (2) `.assessments`: a list of polarity and subjectivity scores for the assessed tokens.The polarity of the document. |



## `spacy.Token` extensions


| Extension | Type | Description |
|-----------|------|-------------|
| doc._.sentiment | `tuple` | Just like in the textblob library, sentiment returns a named tuple: (0) `.polarity`: a float within the range (-1.0, 1.0), (1) `.subjectivity`: a float within the range (0.0, 1.0) where 0.0 is very objective and 1.0 is very subjective, and (2) `.assessments`: a list of polarity and subjectivity scores for the assessed tokens.The polarity of the document. |



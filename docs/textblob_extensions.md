# TextBlob Extensions

## Usage

TextBlob supports adding custom models and new languages through “extensions”. Check out the TextBlob docs ([https://textblob.readthedocs.io/en/dev/extensions.html#extensions](https://textblob.readthedocs.io/en/dev/extensions.html#extensions)) for more details.

*spacytextblob* also supports the use of TextBlob extensions. Use you a TextBlob extension you need to pass some additional information to the `config` parameter when initializing the *spacytextblob* pipeline component.

When using *spacytextblob* without a TextBlob extension your code probably looks something like this:

```python



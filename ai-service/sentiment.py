import os
from google.cloud import language_v1

def analyze_sentiment(text):
    """
    Analyzing Sentiment in a String

    Args:
      text_content The text content to analyze
    """

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:\\Users\\firif\\junction-hack22esp-7028-88114d2e6eae.json"

    client = language_v1.LanguageServiceClient()

    # text_content = 'I am so happy and joyful.'

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text, "type_": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    # Get overall sentiment of the input document
    print(u"Document sentiment score: {}".format(response.document_sentiment.score))
    print(
        u"Document sentiment magnitude: {}".format(
            response.document_sentiment.magnitude
        )
    )
    if response.document_sentiment.score * response.document_sentiment.magnitude < -2:
        return False
    return True

# analyze_sentiment("hello")
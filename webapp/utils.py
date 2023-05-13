from .sentiment.analyzer import SentimentIntensityAnalyzer

def get_score_of_sentiment(text: str) -> float:
    """
    Returns a float score of sentiment of the text.

    :param text: text to analyze
    :return: float score of sentiment
    """
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)['compound']

def get_sentiment(score: float) -> int:
    """
    Returns an integer sentiment of the text.

    :param score: float score of sentiment
    :return: integer sentiment
    """
    if score >= 0.05:
        return 1
    elif score <= -0.05:
        return -1
    else:
        return 0

# Path: webapp\views.py
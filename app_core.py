# app_core.py
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

_analyzer = None

def get_analyzer():
    global _analyzer
    if _analyzer is None:
        _analyzer = SentimentIntensityAnalyzer()
    return _analyzer

def analyze(text: str, analyzer=None):
    text = (text or "").strip()
    if not text:
        return {"label": "NEUTRAL", "score": 0.0, "text": ""}
    analyzer = analyzer or get_analyzer()
    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]  # -1..1
    if compound >= 0.05:
        label = "POSITIVE"
    elif compound <= -0.05:
        label = "NEGATIVE"
    else:
        label = "NEUTRAL"
    # normalize to 0..1 for display
    return {"label": label, "score": (compound + 1) / 2, "text": text}

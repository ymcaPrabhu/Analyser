# tests/test_app.py
from app_core import analyze

class FakeAnalyzer:
    def polarity_scores(self, text):
        text = (text or "").lower()
        if "good" in text:
            return {"compound": 0.9}
        if "bad" in text:
            return {"compound": -0.9}
        return {"compound": 0.0}

def test_empty_is_neutral():
    r = analyze("", analyzer=FakeAnalyzer())
    assert r["label"] == "NEUTRAL" and r["score"] == 0.0

def test_good_is_positive():
    r = analyze("This is good", analyzer=FakeAnalyzer())
    assert r["label"] == "POSITIVE" and r["score"] > 0.5

def test_bad_is_negative():
    r = analyze("This is bad", analyzer=FakeAnalyzer())
    assert r["label"] == "NEGATIVE" and r["score"] < 0.5

from nlplogic.corenlp import get_phrases


def test_get_phrase():
    assert "warriors" in get_phrases("Golden State Warriors")

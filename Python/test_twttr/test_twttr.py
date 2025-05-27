from twttr import shorten

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("AUEIOauieo") == ""
    assert shorten("12345") == "12345"
    assert shorten("Hello, World!") == "Hll, Wrld!"


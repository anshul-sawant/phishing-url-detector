import re
from urllib.parse import urlparse

SUSPICIOUS_WORDS = [
    "login", "verify", "verification", "secure",
    "account", "update", "signin", "password"
]

def extract_features(url):
    parsed = urlparse(url if "://" in url else "http://" + url)
    hostname = parsed.netloc

    features = {
        "url_length": len(url),
        "dot_count": url.count("."),
        "hyphen_count": url.count("-"),
        "digit_count": sum(char.isdigit() for char in url),
        "special_char_count": sum(
            not char.isalnum() and char not in "._-:/"
            for char in url
        ),
        "https": int(parsed.scheme.lower() == "https"),
        "has_ip": int(bool(re.fullmatch(r"\d{1,3}(\.\d{1,3}){3}", hostname))),
        "suspicious_word_count": sum(
            word in url.lower() for word in SUSPICIOUS_WORDS
        ),
    }

    return features

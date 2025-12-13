import hashlib


def md5(utf8: str):
    return hashlib.md5(bytes(utf8, encoding="utf-8")).hexdigest()

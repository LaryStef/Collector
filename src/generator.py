from random import choice
from string import ascii_letters, digits


def generate_id(length: int, only_digits: bool = False) -> str:
    symbols: str = digits

    if not only_digits:
        symbols += ascii_letters

    _id: str = ""

    for _ in range(length):
        _id += choice(symbols)
    return _id

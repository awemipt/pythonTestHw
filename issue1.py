from Variables import LETTER_TO_MORSE


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвии c таблицей азбуки Морзе
    return morse code of message,
    expected english message including special symbols
    raises ValueError if message not str
    KeyError if message contains non specified symbols
    >>> encode('SOS')
    '... --- ...'
    >>> encode(1)
    Traceback (most recent call last):
        ...
    ValueError: message must be str
    >>> encode('ф')
    Traceback (most recent call last):
        ...
    KeyError: 'non specified symbols'
    >>> encode("MORSE CODE")
    '-- --- .-. ... . / -.-. --- -.. .'
    """
    if not isinstance(message, str):
        raise ValueError('message must be str')

    message.upper()
    try:
        encoded_signs = [
            LETTER_TO_MORSE[letter] for letter in message
        ]
    except KeyError:
        raise KeyError('non specified symbols')

    return ' '.join(encoded_signs)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

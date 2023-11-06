from Variables import MORSE_TO_LETTER


def decode(morse_message: str) -> str:
    """
    Декодирует строку из азбуки Морзе в английский
    """
    decoded_letters = [
        MORSE_TO_LETTER[letter] for letter in morse_message.split()
    ]
    print(decoded_letters)
    return ''.join(decoded_letters)


if __name__ == '__main__':
    print(decode('... --- ... / ...'))

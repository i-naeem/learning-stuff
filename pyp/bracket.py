import string


def say(text: str) -> None:
    text = f'[ {text} ]'
    print()
    print(text.center(len(text) + 10))
    print()

print(__name__)


def say(text: str) -> None:
    text = f'[ {text} ]'
    print()
    print(text.center(len(text) + 10))
    print()

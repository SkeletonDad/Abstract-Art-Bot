from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if 'art' in lowered:
        return 'Here is some art!'
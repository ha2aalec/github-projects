import random

def generate_random_code(length=8):
    """Generates a random string of letters and digits.

    Args:
        length (int, optional): The length of the generated string. Defaults to 8.

    Returns:
        str: A random string of letters and digits.
    """
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(characters) for i in range(length))

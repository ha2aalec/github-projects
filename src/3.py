import random
def get_random_python_code():
    """
    Generates a random Python code snippet
    :return: A string of random Python code
    """
    lines = []
    for i in range(0, random.randint(1, 5)):
        line = ""
        for j in range(0, random.randint(3, 6)):
            line += chr(random.randint(97, 122))
        lines.append(line)
    return "\n".join(lines)
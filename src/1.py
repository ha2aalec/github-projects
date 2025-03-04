import random

def get_random_python_code():
    code = f"""
    def main():
        # Generate a random number between 1 and 10
        x = random.randint(1, 10)
        # Print the result
        print(x)

    if __name__ == "__main__":
        main()
    """
    return code
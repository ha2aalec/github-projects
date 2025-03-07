def get_random_python_code():
    # Generate a random number between 1 and 10
    num = random.randint(1, 10)

    # Create a list of possible Python statements
    statements = ['x = 5', 'y = "hello"', 'print("Hello World!")', 'for i in range(5): print(i)']

    # Return a random statement from the list
    return statements[num]

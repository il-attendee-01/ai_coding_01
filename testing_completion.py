def fibonacci(n):
    """
    Generates the Fibonacci sequence up to the nth term.

    Args:
        n (int): The number of terms in the Fibonacci sequence to generate.

    Returns:
        list: A list containing the Fibonacci sequence up to the nth term.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequence = [0, 1] + [sequence[i - 1] + sequence[i - 2] for i in range(2, n)]
    return sequence

print(fibonacci(10))

def factorial(n):
    """
    Computes the factorial of a non-negative integer.

    Args:
        n (int): The non-negative integer to compute the factorial for.

    Returns:
        int: The factorial of the given integer.

    Raises:
        ValueError: If the input is negative.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result

print(factorial(5))

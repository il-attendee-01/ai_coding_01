def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        print([0])
        return [0]
    elif n == 2:
        print([0, 1])
        return [0, 1]

    sequence = [0, 1]
    print(sequence)  # initial state
    for i in range(2, n):
        next_value = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_value)
        print(sequence)  # intermediate result after each iteration

    return sequence

print(fibonacci(10))

def factorial(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result

print(factorial(5))
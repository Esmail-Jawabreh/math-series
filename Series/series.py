# Fibonacci Functions with recursive and iterative.

# def fibonacci_recursive(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


# def fibonacci_iterative(n):
#     if n <= 1:
#         return n
#     else:
#         a, b = 0, 1
#         for _ in range(n-1):
#             a, b = b, a + b
#         return b


def fibonacci(n):
    """
    Return the nth number in the Fibonacci sequence.

    Args:
        n (int): The index of the number to return. Must be a positive integer.

    Returns:
        int: The nth number in the Fibonacci sequence.

    Raises:
        ValueError: If the input n is not a positive integer.

    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(6)
        8
    """
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(n-1):
            a, b = b, a + b
        return b


# Lucas Functions with recursive and iterative.

# def lucas_recursive(n):
#     if n == 0:
#         return 2
#     elif n == 1:
#         return 1
#     else:
#         return lucas_recursive(n-1) + lucas_recursive(n-2)


# def lucas_iterative(n):
#     if n == 0:
#         return 2
#     elif n == 1:
#         return 1
#     else:
#         a, b = 2, 1
#         for _ in range(n-1):
#             a, b = b, a + b
#         return b


def lucas(n):
    """
    Return the nth number in the Lucas sequence.

    Args:
        n (int): The index of the number to return. Must be a non-negative integer.

    Returns:
        int: The nth number in the Lucas sequence.

    Raises:
        ValueError: If the input n is not a non-negative integer.

    Examples:
        >>> lucas(0)
        2
        >>> lucas(1)
        1
        >>> lucas(6)
        18
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        a, b = 2, 1
        for _ in range(n-1):
            a, b = b, a + b
        return b


# sum_series

def sum_series(n, first=0, second=1):
    """
    Prints the nth element in a series.

    Parameters:
    n (int): The index of the element to be printed.
    first (int): The first element in the series. Default value is 0.
    second (int): The second element in the series. Default value is 1.

    Returns:
    int: The nth element in the series.
    """
    if first == 0 and second == 1:
        return fibonacci(n)

    elif first == 2 and second == 1:
        return lucas(n)

    else:
        if n == 0:
            return first
        elif n == 1:
            return second
        else:
            return sum_series(n-1, first, second) + sum_series(n-2, first, second)

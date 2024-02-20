def fibonacci(n):
    """ Calculates the nth term in fibonacci sequence
    Args:
        n (int): Input any positive integer preferrably greater than 1
    
    Return: int: nth term of fibonacci sequence,
             equal to sum of previous two terms
    
    Examples:
        >>> fibonacci(1)
        1        
        >> fibonacci(2)
        1
        >> fibonacci(3)
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
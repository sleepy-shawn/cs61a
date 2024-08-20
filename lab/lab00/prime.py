def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    i = 2 
    result = True
    while i < n:
        if n % i == 0:
            result = False
        i += 1
    if n == 1:
        result = False
    return result 


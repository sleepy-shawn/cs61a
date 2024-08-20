def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    "*** YOUR CODE HERE ***"
    i = 1
    while i <= n:
        print (t(i))
        i+=1
        
def t(i):
    if i % 3 == 0 and i % 5 == 0:
        return("fizzbuzz")
    elif i % 3 == 0:
        return("fizz")
    elif i % 5 == 0:
        return("buzz")
    else:
        return(i)

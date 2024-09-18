def minimum_mewtations(typed, source, limit):
    """A diff function that computes the edit distance from TYPED to SOURCE.
    This function takes in a string TYPED, a string SOURCE, and a number LIMIT.
    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of edits
    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    if limit < 0:
        return 100000000000000
    if typed == source == '':
        return 0    
    elif typed == '':
        return 1 + minimum_mewtations(typed, source[1:], limit - 1)
    elif source =='':
        return 1 + minimum_mewtations(typed[1:], source, limit - 1)
    elif typed[0] == source[0]:
        return 0 + minimum_mewtations(typed[1:], source[1:], limit) 
    else:
        if len(typed) == len(source) == 1:
            return  1 + minimum_mewtations(typed[1:], source[1:], limit - 1)
        else:
            if len(typed) == len(source):
                return 1 + minimum_mewtations(typed[1:], source[1:], limit - 1) #subsititute
            else:
                if typed[1] == source[0]: # remove
                    return 1 + minimum_mewtations(typed[2:], source[1:], limit - 1)
                elif typed[0] == source[1]: #add
                    return 1 + minimum_mewtations(typed[1:],source[2:], limit - 1)  
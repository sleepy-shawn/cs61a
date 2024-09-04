def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    def f(i, who, direction):
        if i == n:
            return who
        else:
            if has_seven(i) or i % 7 == 0:
                direction = -direction
            if direction == 1:
                if who == k:
                    who = 1
                else:
                     who = who + 1
            else:
                if who == 1:
                    who = k
                else:
                    who = who - 1
            i = i + 1
            return f (i,who,direction)

                
            

    return f(1, 1, 1)

def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)

def invert(x):
    print('Never print zero')
    return (1/x)

def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        print('handled', type(e))
        return 0
    
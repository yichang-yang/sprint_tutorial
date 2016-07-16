""" Module to compute stuff
"""


def my_sum(x, y):
    """ Compute the sum of 2 numbers
    """
    return x + y


def my_power(a, n):
    """ Compute a^n """
    pow = a
    for i in range(n-1):
        pow = pow*a

    return pow

def my_root(a, n=2):
    """ Compute the nth root of a """
    res = a**(1.0/n)
    return res

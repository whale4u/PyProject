def avg(first, *rest):
    """
    >>> avg(1, 2)
    1.5
    >>> avg(1, 2, 6)
    3.0
    >>> avg(1, 2, 6, "a")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 2, in avg
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    >>>
    """
    return (first + sum(rest)) / (1 + len(rest))


if __name__ == '__main__':
    # print(avg(1, 2))
    # print(avg(1, 2, 5, 6))
    import doctest
    doctest.testmod()

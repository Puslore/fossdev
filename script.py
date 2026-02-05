def sum(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError('Denominator could not be zero')
    return a / b

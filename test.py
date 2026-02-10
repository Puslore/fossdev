from script import sum, divide


def test_sum():
    a = 1
    b = 2
    assert sum(a, b) == 3


def test_divide():
    a = 2
    b = 4
    result = 0.5
    assert divide(a, b) == result


def test_division_prohibited():
    try:
        divide('A', 'B')
        print('Test string-division false')
        assert False
    except ValueError as err:
        print('Test string-division passed')


def test_divide_by_zero():
    a = 2
    b = 0
    try:
        divide(a, b)
        assert False
    
    except ValueError as err:
        print('Test (division by zero) passed successfully')


if __name__ == "__main__":
    test_divide()
    test_sum()
    test_divide_by_zero()
    test_division_prohibited()

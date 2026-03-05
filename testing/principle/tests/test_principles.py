# import sys
# sys.path.append('../src')
# так делать не надо


# TODO make it with 'pip install -e . math_demo'


from math_demo import (
    add,
    add_with_bug
)


def test_addition():
    assert add(2, 2) == 4
    assert add(0, 0) == 0
    assert add(7, 8) == 15
    print('Test ADDITION PASSED')


def test_addition_with_bug():
    # Тесты показывают наличие ошибок, а не их отсутствие
    assert add_with_bug(2, 2) == 4
    print('Test BUGGED ADDITION PASSED')
    # finally we found data that make test reliable
    # assert add_with_bug(2, 6) == 8 will fail here


if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
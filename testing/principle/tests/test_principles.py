# import sys
# sys.path.append('../src')
# так делать не надо


# TODO make it with 'pip install -e . math_demo'
# in project root dir after setup.py defined

# Раннее тестирование позволяет сэкономить время позднее
# Тесты показывают наличие ошибок, а не отсутсвие
# Тесты не должны дублировать логику тестируемого кода
# ----------------------------------------------------------------------
# Тесты не должны использовать ВСЕ наборы входных параметров
# Тесты должны покрывать "кластеры" входных параметров
# Тесты должны обнаруживать новые ошибки (pescicide paradox)
# Тесты покрывают как успешные, так и ошибочные кейсы


from math_demo import (
    add,
    add_with_bug
)


def test_addition():
    assert add(2, 2) == 4
    assert add(0, 0) == 0
    assert add(7, 8) == 15
    print('Test ADDITION PASSED')


def test_addition_duplicate():
    assert add(6, 7) == 6 + 7
    print('Test DUPLICATE ADDITION PASSED')


def test_addition_with_bug():
    # Тесты показывают наличие ошибок, а не их отсутствие
    assert add_with_bug(2, 2) == 4
    print('Test BUGGED ADDITION PASSED')
    # finally we found data that make test reliable
    # assert add_with_bug(2, 6) == 8 will fail here


if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_duplicate()
# import sys
# sys.path.append('../src')
# так делать не надо


# TODO make it with 'pip install -e . math_demo'
# in project root dir after setup.py defined

# [DONE] Раннее тестирование позволяет сэкономить время позднее
# [DONE] Тесты показывают наличие ошибок, а не отсутсвие

# [DONE] Тесты не должны дублировать логику тестируемого кода

# [DONE] Тесты не должны использовать ВСЕ наборы входных параметров
# Тесты должны покрывать "кластеры" входных параметров
# [DONE] Тестовые функции должны тестировать логические блоки

# [DONE] Тесты должны обнаруживать новые ошибки (pescicide paradox)

# Тесты покрывают как успешные, так и ошибочные кейсы


from math_demo import (
    add,
    add_with_bug,
    calculate_tax,
    claculate_tax_bugged
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


def test_addition_overkill():
    for i in range(0, 2 ** 32):
        for j in range(0, 2 ** 32):
            assert add(i, j) == i + j
            assert add(-i, j) == -i + j
            assert add(i, -j) == i + -j
            assert add(-i, -j) == -i + -j
    print('Test OVERKILL PASSED')


def test_tax_calculator_pesticide():
    assert claculate_tax_bugged(1000) == 150
    assert claculate_tax_bugged(100) == 15
    assert claculate_tax_bugged(10) == 1.5
    assert claculate_tax_bugged(1) == 0.15
    assert claculate_tax_bugged(234) == 35.1
    print('Test TAX CALCULATOR PASSED')
    # float may give us cases
    # not available with using int
    # assert claculate_tax_bugged(2.34) == 0.35



def test_calculate_tax():
    assert calculate_tax(1000) == 150
    assert calculate_tax(100) == 15
    assert calculate_tax(10) == 1.5
    assert calculate_tax(1) == 0.15
    assert calculate_tax(234) == 35.1
    print('Test CALCULATE TAX PASSED')
    assert calculate_tax(2.34) == 0.35


def test_addition_clusters():
    assert add(7, 6) == 13
    assert add(0, 6) == 6
    assert add(7, 0) == 7
    assert add(10, -11) == -1
    assert add(-10, -11) == -21
    assert add(-5, 0) == -5
    assert add(0, -2) == -2
    assert add(5, 9) == 14
    assert add(9, 5) == 14
    print('Test CLUSTERS PASSED')


if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_duplicate()
    # test_addition_overkill() # try it on your risk
    test_addition_clusters()
    test_tax_calculator_pesticide()
    test_calculate_tax()
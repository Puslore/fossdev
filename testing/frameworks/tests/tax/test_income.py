import pytest
from tax.income import calculate_tax


def test_icome_tax():

    assert calculate_tax(100) == 13
    print("TEST TAX PASSED")


def test_calculate_tax_integer_cents():
    assert calculate_tax(10.5) == 1.36


@pytest.mark.parametrize('income, expected', [
                          (100, 13.0),
                          (10.5, 1.36)
])
def test_calculate_tax_parametrized(
    income, expected
):
    assert calculate_tax(income) == expected


if __name__ == "__main__":
    test_icome_tax()

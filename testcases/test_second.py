import pytest


@pytest.mark.parametrize("a,b",[(2,3)])
def test_mul(a, b):
    print(a * b)

@pytest.mark.parametrize("a,b",[(2,3)])
def test_div(a, b):
    print(a / b)





import pytest


@pytest.mark.parametrize("a,b",[(2,3)])
def test_max(a, b):
    print(a if a>b else a)

@pytest.mark.parametrize("a,b",[(2,3)])
def test_square(a, b):
    print(a**a,b**b)





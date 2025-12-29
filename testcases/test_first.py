import pytest


@pytest.mark.parametrize("a,b",[(2,3)])
def test_add(a,b):
    print(a+b)

@pytest.mark.parametrize("a,b",[(2,3)])
def test_minus(a,b):
    print(a+b)





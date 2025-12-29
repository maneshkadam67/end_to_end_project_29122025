import pytest


@pytest.mark.parametrize("a,b,c",[(2,3,5)])
def test_add(a,b,c):
    assert a+b==c

@pytest.mark.parametrize("a",[("message")])
def test_message_assert(a):
    assert a=="message"





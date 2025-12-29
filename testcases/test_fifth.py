import pytest


@pytest.mark.parametrize("status",[(300)])
def test_status(status):
    assert status==300


def test_assert():
    assert True==1





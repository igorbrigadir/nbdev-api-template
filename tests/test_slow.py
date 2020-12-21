import pytest


@pytest.mark.slow
def test_slow():
    pass


@pytest.mark.fast
def test_fast():
    pass

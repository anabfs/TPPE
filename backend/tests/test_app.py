import pytest

@pytest.mark.skip(reason="Ignorado para o primeiro checkpoint.")
def test_exemplo():
    assert 1 + 1 == 2

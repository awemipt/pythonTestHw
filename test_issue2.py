import pytest
from issue2 import decode


@pytest.mark.parametrize('test_input, expected', [
    (' ', ''), ('... --- ...', 'SOS'),
    ('---', 'O'), ('... --- ... / ...', 'SOS S')
])
def test(test_input: str, expected: str):
    assert decode(test_input) == expected
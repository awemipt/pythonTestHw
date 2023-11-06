from issue4 import fit_transform
import pytest


def test_fit_transform_with_no_args():
    with pytest.raises(TypeError):
        fit_transform()


def test_fit_transform_with_single_arg():
    result = fit_transform("apple", "banana", "cherry")
    assert result == [
        ('apple', [0, 0, 1]), ('banana', [0, 1, 0]), ('cherry', [1, 0, 0])
    ]


def test_fit_transform_with_multiple_args():
    result = fit_transform(["apple", "banana", "cherry"])
    assert result == [
        ('apple', [0, 0, 1]), ('banana', [0, 1, 0]), ('cherry', [1, 0, 0])
    ]


def test_fit_transform_with_duplicate_values():
    result = fit_transform("apple", "banana", "cherry", "apple")
    assert result == [
        ('apple', [0, 0, 1]), ('banana', [0, 1, 0]),
        ('cherry', [1, 0, 0]), ('apple', [0, 0, 1])
    ]

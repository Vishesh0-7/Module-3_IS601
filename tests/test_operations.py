import pytest
from app.operations import addition, subtraction, multiplication, division

class TestOperations:

    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (-1, -1, -2)
    ])
    def test_addition(self, a, b, expected):
        assert addition(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (5, 3, 2),
        (0, 0, 0),
        (-1, -1, 0),
        (-1, 1, -2)
    ])
    def test_subtraction(self, a, b, expected):
        assert subtraction(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 6),
        (-1, 1, -1),
        (0, 5, 0),
        (-2, -3, 6)
    ])
    def test_multiplication(self, a, b, expected):
        assert multiplication(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (6, 3, 2),
        (-6, 3, -2),
        (5, 2, 2.5)
    ])
    def test_division(self, a, b, expected):
        assert division(a, b) == expected

    @pytest.mark.parametrize("a, b", [
        (5, 0),
        (0, 0),
        (-3, 0)
    ])
    def test_division_by_zero(self, a, b):
        with pytest.raises(ValueError) as excinfo:
            division(a, b)
        assert str(excinfo.value) == "Division by zero is not allowed."

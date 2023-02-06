from unittest import TestCase
from calculator import Calculator
from unittest.mock import patch


def mock_sum(a, b):
    return a + b


class TestCalculator(TestCase):
    def setUp(self):
        self.calc = Calculator()

    @patch('calculator.Calculator.sum', return_value=9)
    def test_sum(self, mocker):
        answer = self.calc.sum(3, 6)
        self.assertEqual(answer, 9)

    @patch('calculator.Calculator.sum', side_effect=mock_sum)
    def test_sum_2(self, mocker_shocker):
        answer = self.calc.sum(2, 6)
        self.assertEqual(answer, 8)

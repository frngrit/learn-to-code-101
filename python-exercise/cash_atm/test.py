import unittest
from cash_atm import atm

class TestATMFunction(unittest.TestCase):

    def test_atm_with_amount_2500_should_return_proper_banknotes(self):
        # Arrange
        expected_result = {1000: 2, 500: 1, 100: 0}
        amount = 2500
        # Act
        actual_result = atm(amount)
        # Assert
        self.assertEqual(actual_result, expected_result, f'Expected {expected_result}, got {actual_result}')

    def test_atm_with_amount_1300_should_return_proper_banknotes(self):
        # Arrange
        expected_result = {1000: 1, 500: 0, 100: 3}
        amount = 1300
        # Act
        actual_result = atm(amount)
        # Assert
        self.assertEqual(actual_result, expected_result, f'Expected {expected_result}, got {actual_result}')

    def test_atm_with_amount_700_should_return_proper_banknotes(self):
        # Arrange
        expected_result = {1000: 0, 500: 1, 100: 2}
        amount = 700
        # Act
        actual_result = atm(amount)
        # Assert
        self.assertEqual(actual_result, expected_result, f'Expected {expected_result}, got {actual_result}')

    def test_atm_with_zero_amount_should_return_empty_banknotes(self):
        # Arrange
        expected_result = {1000: 0, 500: 0, 100: 0}
        amount = 0
        # Act
        actual_result = atm(amount)
        # Assert
        self.assertEqual(actual_result, expected_result, f'Expected {expected_result}, got {actual_result}')

    def test_atm_with_large_amount_should_return_proper_banknotes(self):
        # Arrange
        expected_result = {1000: 98, 500: 1, 100: 2}
        amount = 98700
        # Act
        actual_result = atm(amount)
        # Assert
        self.assertEqual(actual_result, expected_result, f'Expected {expected_result}, got {actual_result}')

if __name__ == '__main__':
    unittest.main()
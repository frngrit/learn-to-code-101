import unittest

from fizz_buzz import fizz_buzz

class TestFizzBuzzFunction(unittest.TestCase):

    def test_number_divisible_by_15_should_return_FizzBuzz(self):
        # Arrange
        expected_result = "FizzBuzz"
        number = 30
        # Act
        actual_result = fizz_buzz(number)
        # Assert
        self.assertEqual(actual_result, expected_result, f'Expected {expected_result}, got {actual_result}')

    def test_number_divisible_by_5_should_return_Buzz(self):
        # Arrange
        expected_result = "Buzz"
        number = 10
        # Act
        actual_result = fizz_buzz(number)
        # Assert
        self.assertEqual(actual_result, expected_result, f'Expected {expected_result}, got {actual_result}')

    def test_number_divisible_by_3_should_return_Fizz(self):
        # Arrange
        expected_result = "Fizz"
        number = 9
        # Act
        actual_result = fizz_buzz(number)
        # Assert
        self.assertEqual(actual_result, expected_result, f'Expected {expected_result}, got {actual_result}')

    def test_number_not_divisible_by_3_or_5_should_return_dash(self):
        # Arrange
        expected_result = "-"
        number = 7
        # Act
        actual_result = fizz_buzz(number)
        # Assert
        self.assertEqual(actual_result, expected_result, f'Expected {expected_result}, got {actual_result}')

if __name__ == '__main__':
    unittest.main()

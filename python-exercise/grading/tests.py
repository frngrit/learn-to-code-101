import unittest

from grading import grading

class TestGrading(unittest.TestCase):

    def test_grade_80_should_returns_A(self):
        #Arrage
        expect = "A"
        grade = 80
        #Act
        actual = grading(grade)
        #Assert
        self.assertEqual(actual, expect, f'Expected {expect}, got {actual}')

    def test_grade_60_should_returns_B(self):
        #Arrage
        expect = "B"
        grade = 60
        #Act
        actual = grading(grade)
        #Assert
        self.assertEqual(actual, expect, f'Expected {expect}, got {actual}')

    def test_grade_40_should_returns_C(self):
        #Arrage
        expect = "C"
        grade = 40
        #Act
        actual = grading(grade)
        #Assert
        self.assertEqual(actual, expect, f'Expected {expect}, got {actual}')

    def test_grade_30_should_returns_Fail(self):
        #Arrage
        expect = "Fail"
        grade = 30
        #Act
        actual = grading(grade)
        #Assert
        self.assertEqual(actual, expect, f'Expected {expect}, got {actual}')

if __name__ == '__main__':
    unittest.main()

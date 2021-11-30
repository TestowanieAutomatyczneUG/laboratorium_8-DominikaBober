import unittest
from parameterized import parameterized

from .function import fizzbuzz

class Test_fizzBuzz(unittest.TestCase):
	@parameterized.expand([
		(0, "FizzBuzz"),
		(1, "1"),
		(2, "2"),
		(3, "Fizz"),
		(4, "4"),
		(5, "Buzz"),
		(6, "Fizz"),
        (7, "7"),
        (8, "8"),
        (9, "Fizz"),
        (10, "Buzz"),
        (11, "11"),
        (12, "Fizz"),
        (13, "13"),
        (14, "14"),
        (15, "FizzBuzz")
	])

	def test_positive(self, number, expectedOutput):
		self.assertEqual(fizzbuzz(number), expectedOutput)

	@parameterized.expand([
		(21.37, Exception),
		("string", Exception),
		([], Exception),
        ([1, 2, 3], Exception),
        ({}, Exception),
        ({"key": "value"}, Exception)
	])

	def test_exceptions(self, number, expectedError):
		self.assertRaises(expectedError, fizzbuzz, number)
import unittest
from funktioner import add, subtract, check_if_possible_positiv_int

class TestAdditionFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5.0)

    def test_add_zero_and_five(self):
        self.assertEqual(add(0, 5), 5)

    def test_add_five_and_zero(self):
        self.assertEqual(add(5, 0), 5)

    def test_add_zero_and_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)


class TestSubtractionFunction(unittest.TestCase):

    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(2, 3), -1)

    def test_subtract_zero_and_five(self):
        self.assertEqual(subtract(0, 5), -5)

    def test_subtract_five_and_zero(self):
        self.assertEqual(subtract(5, 0), 5)

    def test_subtract_zero_and_zero(self):
        self.assertEqual(subtract(0, 0), 0)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-2, -3), 1)


class TestCheckIfPossibleIntFunction(unittest.TestCase):

    def test_positive_int(self):
        self.assertEqual(check_if_possible_positiv_int(4), True)

    def test_zero_int(self):
        self.assertEqual(check_if_possible_positiv_int(0), True)

    def test_negative_int(self):
        self.assertEqual(check_if_possible_positiv_int(-4), False)

    def test_none_value(self):
        self.assertEqual(check_if_possible_positiv_int(None), False)

    def test_valid_int_string(self):
        self.assertEqual(check_if_possible_positiv_int('123'), True)

    def test_invalid_int_string(self):
        self.assertEqual(check_if_possible_positiv_int('-23'), False)

    def test_invalid_string(self):
        self.assertEqual(check_if_possible_positiv_int('asdf'), False)



if __name__ == "__main__":
    unittest.main()

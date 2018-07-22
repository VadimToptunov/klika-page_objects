import unittest
from utilities import Utilities


class SimpleCalculusTests(unittest.TestCase, Utilities):

    def setUp(self):
        self._set_up()

    def test_insert_digits(self):
        '''Checks if a user can insert 1234567890. '''
        buttons = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        self.click_specified_buttons(buttons)
        self.assertEquals(self.get_values(), "1234567890")
        self.make_screenshot()

    def test_small_multi(self):
        '''Checks if 3 x 3 = 9'''
        buttons = ["3", "x", "3", "="]
        self.click_specified_buttons(buttons)
        self.assertEquals(self.get_values(), "9")
        self.make_screenshot()

    def test_small_division(self):
        ''' Checks if 20 / 5 = 4 '''
        buttons = ["2", "0", "/", "5", "="]
        self.click_specified_buttons(buttons)
        self.assertEquals(self.get_values(), "4")
        self.make_screenshot()

    def test_small_plus(self):
        '''Checks if 1 + 2 = 3'''
        buttons = ["1", "+", "2", "="]
        self.click_specified_buttons(buttons)
        self.assertEquals(self.get_values(), "3")
        self.make_screenshot()

    def test_small_minus(self):
        ''' Checks if 5 - 2 = 3'''
        buttons = ["5", "-", "2", "="]
        self.click_specified_buttons(buttons)
        self.assertEquals(self.get_values(), "3")
        self.make_screenshot()

    def test_insert_double(self):
        ''' Checks one can insert 0.123456789 '''
        buttons = ["0", ".", "1", "2", "3", "4", "5", "6", "7", "8" "9"]
        self.click_specified_buttons(buttons)
        self.assertEquals(self.get_values(), "0.123456789")
        self.make_screenshot()

    def test_double_plus(self):
        ''' Check if 0.5 + 0.25 = 0.75 '''
        buttons = ["0", ".", "5", "+", "0", ".", "2", "5", "="]
        self.click_specified_buttons(buttons)
        self.assertEquals(self.get_values(), "0.75")
        self.make_screenshot()

    def test_double_minus(self):
        ''' Check if 0.5 - 0.25 = 0.25 '''
        buttons = ["0", ".", "5", "-", "0", ".", "2", "5", "="]
        self.click_specified_buttons(buttons)
        self.assertEquals(self.get_values(), "0.25")
        self.make_screenshot()

    def test_double_multi(self):
        ''' Check if 0.5 * 0.5 = 0.25 '''
        buttons = ["0", ".", "5", "x", "0", ".", "2", "5", "="]
        self.click_specified_buttons(buttons)
        self.assertEquals(self.get_values(), "0.25")
        self.make_screenshot()

    def test_double_division(self):
        ''' Check if 0.75 / 0.5 = 1.5 '''
        buttons = ["0", ".", "7", "5", "/", "0", ".", "5", "="]
        self.click_specified_buttons(buttons)
        self.assertEquals(self.get_values(), "1.5")
        self.make_screenshot()

    def test_insert_negative(self):
        ''' Check one can insert a -6 '''
        buttons = ["-", "6"]
        self.click_specified_buttons(buttons)
        self.assertEquals(self.get_values(), "-6")
        self.make_screenshot()

    def test_get_negative(self):
        ''' Checks if 3 - 23 = -20 '''
        buttons = ["3", "-", "2", "3", "="]
        self.click_specified_buttons(buttons)
        self.assertEquals(self.get_values(), "-20")
        self.make_screenshot()

    def test_get_positive_from_negative(self):
        ''' Checks if (3 - 23) + 32 = 12 '''
        buttons = ["3", "-", "2", "3", "+", "3", "2" "="]
        self.click_specified_buttons(buttons)
        self.assertEquals(self.get_values(), "12")
        self.make_screenshot()

    def test_get_negative_double(self):
        ''' Checks if 1,5 - 2 = -0,5 '''
        buttons = ["1", ".", "5", "-", "2", "="]
        self.click_specified_buttons(buttons)
        self.assertEquals(self.get_values(), "-0.5")
        self.make_screenshot()

    def test_negative_plus(self):
        ''' Check if -6 + -3 = -9 '''
        buttons = ["-", "6", "+", "-", "3", "="]
        self.click_specified_buttons(buttons)
        self.assertEquals(self.get_values(), "-9")
        self.make_screenshot()

    def test_negative_substraction(self):
        ''' Check if -6 - -3 = -3 '''
        buttons = ["-", "6", "-", "-", "3", "="]
        self.click_specified_buttons(buttons)
        self.assertEquals(self.get_values(), "-3")
        self.make_screenshot()

    def test_negative_division(self):
        ''' Check if -20 / -5 = 4 '''
        buttons = ["-", "2", "0", "/", "-", "5", "="]
        self.click_specified_buttons(buttons)
        self.assertEquals(self.get_values(), "4")
        self.make_screenshot()

    def test_divide_negative_on_positive(self):
        ''' Check -20 / 4 = -5 '''
        buttons = ["-", "2", "0", "/", "4", "="]
        self.click_specified_buttons(buttons)
        self.assertEquals(self.get_values(), "-5")
        self.make_screenshot()

    def test_divide_positive_on_negative(self):
        ''' Check if 20 / -4 = -5 '''
        buttons = ["2", "0", "/", "-", "4", "="]
        self.click_specified_buttons(buttons)
        self.assertEquals(self.get_values(), "-5")
        self.make_screenshot()

    def test_multiply_negatives(self):
        ''' Check if -5 * -4 = 20 '''
        buttons = ["-", "5", "x", "-", "4", "="]
        self.click_specified_buttons(buttons)
        self.assertEquals(self.get_values(), "20")
        self.make_screenshot()

    def test_multiply_negative_and_positive(self):
        ''' Check if -5 * 4 = -20 '''
        buttons = ["-", "5", "x", "4", "="]
        self.click_specified_buttons(buttons)
        self.assertEquals(self.get_values(), "-20")
        self.make_screenshot()

    def test_check_clear(self):
        '''
        Checks if "C" button works.

        First: insert 5
        Then click "C" button
        Expected result: No values in display field
        '''
        buttons = ["5", "C"]
        self.click_specified_buttons(buttons)
        self.assertEquals(self.get_values(), "")
        self.make_screenshot()

    def test_check_all_clear(self):
        '''
        Checks "AC" button works

        First: insert 5 - 3
        Then: Click "AC"
        Then: insert +6 * 6 =
        Expected result: 36
        '''
        buttons = ["5", "-", "3", "AC", "+", "6", "x", "6", "="]
        self.click_specified_buttons(buttons)
        self.assertEquals(self.get_values(), "36")
        self.make_screenshot()

    def test_zero_division(self):
        '''
        Checks one cannot divide by ZERO

        First: insert 7 / 0
        Expected result: Infinity
        '''
        buttons = ["7", "/", "0", "="]
        self.click_specified_buttons(buttons)
        self.assertEquals(self.get_values(), "Infinity")
        self.make_screenshot()

    def test_zero_divided(self):
        ''' Check if 0 / 5 = 0 '''
        buttons = ["0", "/", "5", "="]
        self.click_specified_buttons(buttons)
        self.assertEquals(self.get_values(), "0")
        self.make_screenshot()

    def tearDown(self):
        self.click_specified_buttons(buttons=["AC"])
        self._tear_down()


if __name__ == "__main__":
    unittest.main()

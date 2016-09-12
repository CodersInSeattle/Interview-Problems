import pytest

from leetcode.math import lc273_integer_to_english_words


class TestNumberToWords(object):
    """ Test the number to words function. """

    SOLUTION = lc273_integer_to_english_words.Solution()

    def test_zero(self):
        number = 0
        assert self.SOLUTION.number_to_words(number) == 'Zero'

    def test_negative(self):
        number = -1
        with pytest.raises(ValueError):
            self.SOLUTION.number_to_words(number)

    def test_large_number(self):
        number = 2**32
        with pytest.raises(ValueError):
            self.SOLUTION.number_to_words(number)

    def test_trailing_zero(self):
        number = 10000000
        assert self.SOLUTION.number_to_words(number) == 'Ten Million'

    def test_full_of_numbers(self):
        number = 2134435666
        assert self.SOLUTION.number_to_words(number) == 'Two Billion One Hundred Thirty Four Million Four Hundred ' \
                                                        'Thirty Five Thousand Six Hundred Sixty Six'

    def test_below_one_thousand(self):
        number = 434
        assert self.SOLUTION.number_to_words(number) == 'Four Hundred Thirty Four'

    def test_zeros(self):
        number = 101010101
        assert self.SOLUTION.number_to_words(number) == 'One Hundred One Million Ten Thousand One Hundred One'

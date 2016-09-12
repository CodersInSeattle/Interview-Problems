"""
Convert a non-negative integer to its english words representation.
Given input is guaranteed to be less than 2^31 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

"""

import math


class Solution(object):

    THOUSAND = 1000
    HUNDRED = 100

    DIVISION_TO_SUFFIX = {
        0: '',
        1: 'Thousand',
        2: 'Million',
        3: 'Billion'
    }

    INT_TO_ENGLISH = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen',
        20: 'Twenty',
        30: 'Thirty',
        40: 'Forty',
        50: 'Fifty',
        60: 'Sixty',
        70: 'Seventy',
        80: 'Eighty',
        90: 'Ninety'
    }

    def number_to_words(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num < 0 or num > 2**31 - 1:
            raise ValueError('Invalid input: num must be non-negative and less than 2^31 - 1')

        if num == 0:
            return 'Zero'

        # fast track
        try:
            return self.INT_TO_ENGLISH[num]
        except KeyError:
            pass

        # keep dividing...
        division_count = 0
        words = []

        while num > 0:
            # change / to //
            num, residual = num // self.THOUSAND, num % self.THOUSAND
            if residual:
                words.insert(0, self._helper(residual, suffix=self.DIVISION_TO_SUFFIX[division_count]))
            division_count += 1
        return ' '.join(words)

    def _helper(self, num, suffix=''):
        """num is less than 1000"""

        if num == 0:
            return ''

        words = []

        # get hundreds
        hundreds = num // self.HUNDRED
        if hundreds:
            words.append(self.INT_TO_ENGLISH[hundreds])
            words.append('Hundred')

        # get last two digits
        last_two = num % self.HUNDRED
        if last_two:
            # fast track if possible
            try:
                words.append(self.INT_TO_ENGLISH[last_two])
            except KeyError:
                ones = num % 10
                tens = (num % self.HUNDRED) - ones
                if tens:
                    words.append(self.INT_TO_ENGLISH[tens])
                if ones:
                    words.append(self.INT_TO_ENGLISH[ones])

        # apply suffix
        if suffix:
            words.append(suffix)
        return ' '.join(words)

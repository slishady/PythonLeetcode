class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = [0] + digits
        m = len(digits) - 1
        digits[m] = digits[m] + 1
        while  m - 1 >= 0 and digits[m]> 9:
            digits[m] = digits[m] - 10
            digits[m-1] += 1
            m -= 1
        if digits[0] == 0:
            return digits[1:]
        else:
            return digits
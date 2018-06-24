class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        a = [[]for i in range(numRows)]
        r = 0
        direction = 1
        for i in s:
            a[r].append(i)
            if r == numRows - 1:
                direction = -1
            elif r == 0:
                direction = 1
            r += direction
        res = ""
        for row in a:
            for col in row:
                res += col
        return res

a = Solution()
print(a.convert("PAYPALISHIRING", 3))
print(a.convert("ABC", 1))



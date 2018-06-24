class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        data = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        if 'CD' in s:
            result += 400
            s = s.replace("CD", "")
        elif 'CM' in s:
            result += 900
            s = s.replace("CM", "")
        if 'XL' in s:
            result += 40
            s = s.replace("XL", "")
        elif 'XC' in s:
            result += 90
            s = s.replace("XC", "")
        if 'IV' in s:
            result += 4
            s = s.replace("IV", "")
        elif 'IX' in s:
            result += 9
            s = s.replace("IX", "")
        for i in set(s):
            result += data[i]*(s.count(i))
        return result

a = Solution()
print(a.romanToInt("III"))
print(a.romanToInt("IV"))
print(a.romanToInt("IX"))
print(a.romanToInt("LVIII"))
print(a.romanToInt("MCMXCIV"))

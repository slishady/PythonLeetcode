class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str[0].isdigit():
            if str[0] != '-' and str[0] != '+':
                return 0
        res = str[0]
        i = 1
        while i < len(str):
            if not str[i].isdigit():
                break
            res += str[i]
            i += 1
        ans = int(res)
        if ans > 2**31 -1 :
            ans = 2**31 - 1
        elif ans < -(2**31):
            ans = -2**31
        return ans

a = Solution()
print(a.myAtoi("-42"))
print(a.myAtoi("4971 i love you"))
print(a.myAtoi("     7 90"))
print(a.myAtoi("words and 971"))
print(a.myAtoi("-91283472332"))
print("MMM".count('M'))
print(set("MMIII"))
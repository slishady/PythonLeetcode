class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = 0
        res = ""
        step = 0
        large = max(a, b ,key=len)
        small = min(a, b, key=len)
        if large == small:
            large = a
            small = b
        i = len(large) - 1
        j = len(small) - 1
        while i >= 0  and j >= 0:
            ans = int(large[i]) + int(small[j]) + step
            if ans > 1:
                res = str(ans-2) + res
                step = 1
            else:
                step = 0
                res = str(ans) + res
            i -= 1
            j -= 1
        while i >= 0:
            if step == 0:
                res = large[:i+1] + res
                break
            else:
                ans = int(large[i]) + step
                if ans > 1:
                    res = str(ans-2) + res
                    step = 1
                    i -= 1
                else:
                    res = large[:i] + str(ans) + res
                    step = 0
                    break
        if step == 1:
            res = "1" + res
        return res

a = Solution()
print(a.addBinary("1010", "1011"))
print(a.addBinary("1111", "1111"))
print(a.addBinary("101111","10"))
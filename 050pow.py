class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        jet = 0
        if n < 0:
            jet = 1
            n = -n
        if n == 0:
            return 1
        elif n%2 == 1:
            ans = x*(self.myPow(x**2, n//2))
        else:
            ans = (self.myPow(x**2, n//2))**2
        if jet == 1:
            return 1/ans
        else:
            return ans
print(-2**31)
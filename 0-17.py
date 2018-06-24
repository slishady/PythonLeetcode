class Solution:
    def __init__(self):
        self.data = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return [""]
        L = []
        self.length = len(digits)
        self.helper(L, digits, "")
        return L


    def helper(self, L, d, s):
        # t = s  
        # for i in self.data[d[0]]:
        #     s = t
        #     s += i
        #     if len(s) == self.length:
        #         L.append(s)
        #     else:
        #         self.helper(L, d[1:], s)

    def helper(self, L, d, s):
        if len(s) == self.length:
            L.append(s)
        else:
            for i in self.data[d[0]]:
                s += i
                self.helper(L, d[1:], s)

a = Solution()
print(a.letterCombinations("23"))
print(a.letterCombinations(""))
print(a.letterCombinations('2'))

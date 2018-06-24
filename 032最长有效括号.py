class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        start = 0
        end = 0
        pole = 1
        maxlen = 0
        while i < len(s):
            if pole and s[i] == '(':
                start = i
                end = i
                pole = 0
            elif s[i] == ')':
                if s[start:end+1].count('(') >= s[start:end+1].count(')'):
                    end += 1
                else:
                    pole = 1


            i += 1
            maxlen = max(maxlen, end - start +1)

        return maxlen

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        start = 0
        end = 0
        pole = 1
        maxlen = 0
        onemax = 0
        pole2 = 0
        while i < len(s):
            if pole and s[i] == '(':
                start = i
                end = i
                pole = 0
            elif s[i] == '(':
                end += 1
            elif s[i] == ')':
                if i-onemax-1 >= 0 and s[i-onemax-1] == '(':
                    onemax += 2
                    end += 1
                else:
                    pole = 1
                    maxlen = max(onemax, maxlen)
                    onemax = 0
            i += 1
            maxlen = max(onemax, maxlen)

        return maxlen

class Solution:
    def longestValidParentheses(self, s):
        max_len = 0
        dp = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                dp.append(i)
            else:
                dp.pop()
                if(len(dp) == 0):
                    dp.append(i)
                else:
                    max_len = max(max_len, i - dp[-1])

        return max_len

class Solution:
    def longestValidParentheses(self, s):
        s = ')' + s
        res = 0
        dp = [0 for _ in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1-dp[i-1]] == '(':
                    dp[i] = dp[i-1] + 2
                if i-dp[i] <= 0:
                    dp[i] += dp[0]
                else:
                    dp[i] += dp[i-dp[i]]

            res = max(res, dp[i])
        return res

a = Solution()
print(a.longestValidParentheses("()"))
print(a.longestValidParentheses(")()())"))
print(a.longestValidParentheses("()(()"))
print(a.longestValidParentheses(")("))
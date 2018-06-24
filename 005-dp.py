class Solution:
    def longestPalindrome(self, s):
        maxlen = 0
        start = 0
        for i in range(len(s)):
            if i - maxlen - 1>=0 and s[i-maxlen-1 : i+1] == s[i-maxlen-1: i+1][::-1]:
                start = i-maxlen-1
                maxlen += 2
                continue    
            if i - maxlen >= 0 and s[i-maxlen: i+1] == s[i-maxlen: i+1][::-1]:
                start = i - maxlen
                maxlen += 1
        return s[start:start+maxlen]
            
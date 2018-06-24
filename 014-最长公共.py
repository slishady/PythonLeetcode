class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        index = 1
        if strs == []:
            return ""
        minlen = min(map(len, strs))
        count = 0
        while index <=  minlen:
            jet = 1
            for i in strs[1:]:
                if not i.startswith(strs[0][:index]):
                    jet = 0
                    index -= 1
                    break
            if jet == 0:
                break
            index += 1
            count += 1
        if count == 0:
            return ""
        if index > minlen:
            index = minlen
        return strs[0][:index]

a = Solution()
print(a.longestCommonPrefix(["flower","flow","flight"]))
print(a.longestCommonPrefix(["dog","racecar","car"]))
print(a.longestCommonPrefix([]))
print(a.longestCommonPrefix(["aa", "a"]))


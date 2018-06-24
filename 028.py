

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len1 = len(haystack)
        len2 = len(needle)
        if len1 >= len2:
            #每次固定一个指针，移动另一个指针去判定
            for i in range(len1 - len2 + 1):
                match = True
                for j in range(len2):
                    #如果有片段不相符
                    if haystack[i + j] != needle[j]:
                        match = False
                        break
                #如果符合，return那个固定的指针
                if match:
                    return i
        return -1
        


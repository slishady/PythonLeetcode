# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         count = 0
#         L = {}
#         max = 0
#         if len(s) == 1:
#             return 1
#         for index, value in enumerate(s):
#             if value in L.values():
#                 if count > max:
#                     max = count
#                 L = {}
#                 count = 1
#             else:
#                 count = 1
#                 L[index] = value
#                 for i in range(index+1, len(s)):
#                     if s[i] in L.values():
#                         if count > max:
#                             max = count
#                         L = {}
#                         break
#                     else:
#                         count += 1
#                         L[i] = s[i]
#                         if count > max:
#                             max = count
#         return max
# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         record_place = {}
#         max_len = 0
#         mid_max_len = 0
#         for (i, ch) in enumerate(s):
#             if ch not in record_place:
#                 mid_max_len += 1
#                 if max_len < mid_max_len:
#                     max_len = mid_max_len
#             else:
#                 if i - record_place[ch] > mid_max_len:
#                     mid_max_len += 1
#                     if mid_max_len > max_len:
#                         max_len = mid_max_len
#                 else:
#                     mid_max_len = i - record_place[ch]

#             record_place[ch] = i
#         return max_len

# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if len(s)==0:
#             return 0
#         loc = {}
#         re = 0
#         sta = 0
#         for i in range(0,len(s)):
#             if s[i] in loc and sta <= loc[s[i]]:    # 注意第二个条件！！ 
#                 sta = loc[s[i]]+1                        #调整开始位置
#                 loc[s[i]]=i                                  #改变loc值
#             else:
#                 loc[s[i]]=i                                  #增加新字符的位置信息
#                 if i-sta+1 > re:                          #compare the length (current loc - start loc)
#                     re = i - sta + 1
#         return re 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        one_max = 0
        data = {}
        start = 0
        for i in range(len(s)):
            if s[i] in data and data[s[i]] >= start:
                start = data[s[i]] + 1
            one_max = i - start + 1
            data[s[i]] = i
            max_len = max(max_len, one_max)
        return max_len

                



a= Solution()
print(a.lengthOfLongestSubstring("abba"))
print(a.lengthOfLongestSubstring("pwwkew"))
print(a.lengthOfLongestSubstring("abcabcbb"))
print(a.lengthOfLongestSubstring("bbbbb"))
print(a.lengthOfLongestSubstring(""))
print(a.lengthOfLongestSubstring("dvdf"))
print(a.lengthOfLongestSubstring("b"))
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans_list = []
        strs.sort(key=sorted)
        i = 0
        count = 0
        while i < len(nums):
            j = i + 1
            while sorted(nums[i]) == sorted(nums[j]):
                j += 1
            ans_list.append(nums[i:j])
            i = j

        return ans_list




             
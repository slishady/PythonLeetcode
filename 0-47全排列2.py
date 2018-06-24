class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        Solution.len = len(nums)
        ans_list = []
        nums.sort()
        self.DFS(nums, ans_list, 0, [])
        return ans_list

    def DFS(self, nums, ans_list, start, valuelist):
        if Solution.len == len(valuelist) and valuelist not in ans_list:
            ans_list.append(valuelist)
        else:
            for i in range(start, len(nums)):
                self.DFS(nums[:i] + nums[i+1:], ans_list, i+1, valuelist+[nums[i]])
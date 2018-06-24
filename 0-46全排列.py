class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        Solution.ans_list = []
        nums.sort()
        Solution.length = len(nums)
        self.DFS(nums, [])

    def DFS(self, nums, valuelist):
        if len(valuelist) == Solution.length:
            Solution.ans_list.append(valuelist)
        else:
            for i in nums:
                self.DFS(nums[:nums.index(i)]+nums[nums.index(i)+1:], valuelist+[i])

        
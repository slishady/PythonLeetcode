class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if 0 < nums[i] and nums[i]< len(nums):
                if nums[i] != nums[nums[i]-1]:
                    while nums[i] != i + 1:
                        nums[nums[i]-1], nums[i] = nums[i], nums[nums[i] - 1]
                        if nums[i] < 0 or nums[i] >= len(nums):
                            break
     

        ans = 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                ans = i + 1
                break
        return ans


a = Solution()
print(a.firstMissingPositive([7,8,9,11,12]))



class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        return (len(nums))


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #先让数组变得有序
        nums.sort()
        if val not in nums:
            return len(nums)
        #找左边第一个目标索引
        posleft = nums.index(val)
        #找右边第一个目标索引
        posright = "".join(map(str, nums)).rfind(str(val))
        #删除
        nums[posleft:posright+1] = []
        return len(nums)

a = Solution()
print(a.removeElement([3,2,2,3], 3))
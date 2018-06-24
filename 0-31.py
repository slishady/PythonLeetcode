class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        if len(list(set(nums))) != 1:
            
            while i - 1 >= 0:
                if nums[i] <= nums[i - 1]:
                    i = i - 1
                else:
                    break
            if i - 1 >= 0:
                j = i - 1

                t = i
                while i < len(nums) - 1:
                    if nums[i] > nums[j] and i < len(nums)-1:
                        i += 1
                    else:
                        i -= 1
                        break
                if nums[i] <= nums[j]:
                    i = i - 1
                nums[i], nums[j] = nums[j], nums[i]
                a = sorted(nums[t:])
                print(a)
                a_index = 0
                for index in range(t, len(nums)):
                    nums[index] = a[a_index]
                    a_index += 1
                print(nums)
            else:
                nums.sort()

L = [2,2,7,5,4,3,2,2,1]
a = Solution()
a.nextPermutation(L)
print(L)

         
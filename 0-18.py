# class Solution:
#     def fourSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         nums.sort()
#         finalans = []
#         for i in range(len(nums) - 3):
#             if nums[i] > target and nums[i]>0:
#                 break
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             for j in range(i+1, len(nums) - 2):
#                 if nums[j] > target and nums[i] > 0:
#                     break
#                 if j > 0 and nums[j] == nums[j-1] and j - 1 != i:
#                     continue
#                 k = j + 1 
#                 l = len(nums) - 1
#                 while k < l:
#                     ans = nums[i] + nums[j] + nums[k] + nums[l]
#                     if ans == target:
#                         finalans.append([nums[i], nums[j], nums[k], nums[l]])
#                         while k < l and nums[k] == nums[k+1]:
#                             k += 1
#                         while k < l and nums[l] == nums[l-1]:
#                             l -= 1
#                         k += 1
#                         l -= 1
#                     elif ans > target:
#                         l -=1
#                     else:
#                         k += 1

#         return finalans
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = set()
        sumans = {}
        if len(nums) < 4:
            return []
        for i in range(2, len(nums) - 1):
            for j in range(i+1, len(nums)):
                onesum = nums[i] + nums[j]
                if onesum not in sumans:
                    sumans[onesum] = [(i, j)]
                else:
                    sumans[onesum].append((i, j))
        for i in range(len(nums) - 3):
            for j in range(i+1, len(nums) - 2):
                onesum = nums[i] + nums[j]
                if target - onesum in sumans:
                    for k in sumans[target - onesum]:
                        if k[0] > j:
                            ans.add((nums[i], nums[j], nums[k[0]], nums[k[1]]))
        return [i for i in ans]


a = Solution()
print(a.fourSum([1, 0, -1, 0, -2, 2], 0))
print(a.fourSum([0, 0, 0, 0], 0))
print(a.fourSum([-1, 0, 1, 2, -1, -4], -1))
print(a.fourSum([1,-2,-5,-4,-3,3,3,5], -11))


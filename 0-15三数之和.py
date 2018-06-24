# class Solution:
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         ans = list()
#         data = {}
#         for i in range(1, len(nums)):
#             if 0 - nums[i] in data:
#                 for k in data[0 - nums[i]]:
#                     if sorted([nums[i]] + k) not in ans:
#                         ans.append(sorted([nums[i]]+k))
#             for j in range(i):
#                 if nums[i] + nums[j] in data:
#                     data[nums[i] + nums[j]].append([nums[i], nums[j]])
#                 else:
#                     data[nums[i] + nums[j]] = [[nums[i], nums[j]]]
#         return ans
# a = Solution()
# print(a.threeSum([-1, 0, 1, 2, -1, -4]))
# class Solution:
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         ans = list()
#         data = {}
#         data[0] = nums[0]
#         data[1] = nums[1]
#         for i in range(2, len(nums)):
#             for j in data.values():
#                 if 0 - nums[i] - j in data.values() :
#                     ans.append([nums[i], j, 0 - nums[i] - j])
#             data[i] = nums[i]
#         return ans

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                while j < k and nums[j] == nums[j+1]:
                    j += 1
                while j < k and nums[k] == nums[k - 1]:
                    k -= 1
                j += 1
                k -= 1
        return ans

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 存储结果列表
        res_list = []
        # 对nums列表进行排序，无返回值，排序直接改变nums顺序
        nums.sort()
        for i in range(len(nums)):
            # 如果排序后第一个数都大于0，则跳出循环，不可能有为0的三数之和
            if nums[i] > 0:
                break
            # 排序后相邻两数如果相等，则跳出当前循环继续下一次循环，相同的数只需要计算一次
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 记录i的下一个位置
            j = i + 1
            # 最后一个元素的位置
            k = len(nums) - 1
            while j < k:
                # 判断三数之和是否为0
                ans = nums[i] + nums[j] + nums[k]
                if ans == 0:
                    # 把结果加入数组中
                    res_list.append([nums[i], nums[j], nums[k]])
                    # 判断j相邻元素是否相等，有的话跳过这个
                    while j < k and nums[j] == nums[j+1]: j += 1
                    # 判断后面k的相邻元素是否相等，是的话跳过
                    while j < k and nums[k] == nums[k-1]: k -= 1
                    # 没有相等则j+1，k-1，缩小范围
                    j += 1
                    k -= 1
                # 小于-nums[i]的话还能往后取
                elif ans < 0:
                    j += 1
                else:
                    k -= 1
        return res_list

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #建立一个空的结果list
        res_list = []
        #对数组排序
        nums.sort()
        #对第一个指针遍历，在思路里说过
        for i in range(len(nums)):
            #第二个指针
            j = i + 1
            #第三个指针
            k = len(nums)- 1
            #第一个最小的数都大于0了，我们后面就不用求了
            if nums[i] > 0:
                break
            if i > 0 and nums[i-1] == nums[i]:
                continue
            #相等的数的符合条件的解在前一个值上已经被求过了
            #往中间夹逼
            while j < k:
                #如果刚好符合条件？
                ans = nums[i] + nums[j] + nums[k]
                if ans == 0:
                    #跳过相同的数
                    res_list.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    #最终都要指向下一个
                    k -= 1
                    j += 1
                #因为数组的有序性，所以我们面对小于Target的情况，应该增大我们目前的值，所以加大j
                elif ans < 0:
                    j += 1
                #同理
                else:
                    k -= 1

        return res_list
a = Solution()
print(a.threeSum([-1,0,1,2,-1,-4]))
            
        
            
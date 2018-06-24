class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        finalans = [nums[0] + nums[1] + nums[2]]
        if nums[0] + nums[1] + nums[2] > target:
            return finalans[0]

        for i in range(len(nums)):
            if nums[i]>0 and nums[i] > target :
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                ans = nums[i] + nums[j] + nums[k]
                if ans == target:
                    return target
                if ans not in finalans:
                    finalans.append(ans)
                if ans > target:
                    k -= 1
                    while j < k - 1 and nums[k] == nums[k-1]: k-=1
                else:
                    j += 1
                    while j < k - 1 and nums[j] == nums[j+1]: j+=1
                # if k == j:
                #     ans = nums[i] + nums[j] + nums[k]
                #     if ans not in finalans:
                #         finalans.append(ans)
        return sorted(finalans, key=lambda x: abs(x - target))[0]

class Solution:#改良版
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = sum(nums[:3])
        if result == target:
            return result
        minDiff = abs(target - result)
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                ans = nums[i] + nums[j] + nums[k]
                if ans == target:
                    return ans
                if abs(target - ans) < minDiff:
                    result = ans
                    minDiff = abs(target - abs)
                if ans > target:
                    k -= 1
                    while j < k - 1 and nums[k] == nums[k-1]: k-=1
                else:
                    j += 1
                    while j < k - 1 and nums[j] == nums[j+1]: j+=1

        return result

                
                 

a = Solution()
print(a.threeSumClosest([-1, 2, 1 , -4], 1))
print(a.threeSumClosest([-1,0,1,1,55], 3))
print(a.threeSumClosest([6,-18,-20,-7,-15,9,18,10,1,-20,-17,-19,-3,-5,-19,10,6,-11,1,-17,-15,6,17,-18,-3,16,19,-20,-3,-17,-15,-3,12,1,-9,4,1,12,-2,14,4,-4,19,-20,6,0,-19,18,14,1,-15,-5,14,12,-4,0,-10,6,6,-6,20,-8,-6,5,0,3,10,7,-2,17,20,12,19,-13,-1,10,-1,14,0,7,-3,10,14,14,11,0,-4,-15,-8,3,2,-5,9,10,16,-4,-3,-9,-8,-14,10,6,2,-12,-7,-16,-6,10]
,-52))


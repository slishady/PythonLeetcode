class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.list = nums
        self.ans = []
        if len(nums) == 1:
            return 0
        if nums[0] >= len(nums) - 1:
            return 1
        self.search(0, 0)

        return min(self.ans)

        
    def search(self, start, count):
        if self.list[start] + start >= len(self.list) - 1:
            count += 1
            self.ans.append(count)
        else:
            for j in range(start+1, start + self.list[start]+1):
                self.search(j, count+1)

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.list = nums
        self.ans = []
        if len(nums) == 1:
            return 0
        if nums[0] >= len(nums) - 1:
            return 1


class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        i = 0
        if len(nums) == 1:
            return 0
        pos = nums[i]
        while i < len(nums):
            step = nums[i]
            if i == len(nums)-1:
                break
            if i + step >= len(nums) - 1:
                count += 1
                break
            candidates = nums[i+1: i+1+step]
            for j in range(len(candidates)):
                if candidates[j] >= len(nums) - 1 - (i + j + 1):
                    count += 2
                    return count
                if candidates[j] + (i+j+1) >= pos:
                    pos = candidates[j] + (i+j+1)
                    candidator = j
            i = i + candidator + 1
            count += 1
        return count
        


a = Solution()
print(a.jump([5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]))
print(a.jump([9,7,9,4,8,1,6,1,5,6,2,1,7,9,0]))
print(a.jump([2,3,1,1,4]))
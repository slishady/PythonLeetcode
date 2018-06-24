#DFS TLE
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        #初始化数组，让它能被用
        self.nums = nums
        #开始位置
        startpos = 0
        nextBound = startpos + nums[startpos]
        nextBound = min(len(self.nums)-1, nextBound)
        for i in range(startpos+1, nextBound+1):
            if i == len(self.nums) - 1:
                return True
            if self.nums[i] == 0:
                continue
            result = self.DFS(i, nextBound)
            if result == True:
                return True
        return False

    def DFS(self, startpos, nextBound):
        if startpos == len(self.nums)-1:
            return True
        if self.nums[startpos] == 0:
            if startpos < nextBound:
                self.DFS(startpos+1, nextBound)
            else:
                return False
        nextBound = startpos + self.nums[startpos]
        nextBound = min(len(self.nums)-1, nextBound)
        for nextIndx in range(startpos+1, nextBound+1):
            result = self.DFS(nextIndx, nextBound)
            if result == True:
                return True

#acquistive
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxPos = 0
        for i in range(len(nums) - 1):
            maxPos = max(maxPos, i+nums[i])
            #如果maxPos == i，说明maxPos < len(nums) - 1, 远位达到终点
            #如果下面这句if成立，说明我们在i 之前的index上所能达到的最远index在i 上没有长进，并且还未达到终点。
            if maxPos == i:
                return False
        return True


#dp
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        maxPos = 0
        for i in range(len(nums)-1):
            #如果历史最高高度达不到我们目前的index
            if maxPos < i:
                return False
            if i == len(nums) - 2 and nums[i] != 0:
                return True
            maxPos = max(maxPos, nums[i] + i)



a = Solution()

print(a.canJump([2,5,0,0]))

    
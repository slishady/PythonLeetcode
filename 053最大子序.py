class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0 
        j = len(nums) - 1
        maxval = nums[0]
        while i < j:
            while i < j and nums[i] <= 0:
                i += 1
            while i < j and nums[j] <= 0:
                j -= 1
            maxval = max(maxval, sum(nums[i:j]))
            if i < j and nums[i] < nums[i+1]:
                i += 1
            if i < j and nums[i+1] < 0:
                i += 2
            if i < j and nums[j] 

        return maxval


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        MaxSum = nums[0]
        for i in range(len(nums)):
            sum += nums[i]
            if sum > MaxSum:
                MaxSum = sum
            if sum < 0:
                sum = 0
        return MaxSum


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        onesum = 0
        maxsum = nums[0]
        for i in range(len(nums)):
            onesum += nums[i]
            maxsum = max(maxsum, onesum)
            if onesum < 0:
                onesum = 0
        return maxsum

  
    def maxSubArray(self, nums):  
        """ 
        :type nums: List[int] 
        :rtype: int 
        """  
        length=len(nums)  
        for i in range(1,length):  
            #当前值的大小与前面的值之和比较，若当前值更大，则取当前值，舍弃前面的值之和  
            subMaxSum=max(nums[i]+nums[i-1],nums[i])  
            nums[i]=subMaxSum#将当前和最大的赋给nums[i]，新的nums存储的为和值  
        return max(nums) 
a = Solution()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
            
            


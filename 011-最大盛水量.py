class Solution:
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        maxval = 0
        while i < j:
            maxval = max(maxval, min(height[i], height[j])*(j-i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxval

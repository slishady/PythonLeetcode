class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        if len(height) <= 2:
            return 0
        for i in range(0, len(height)-1):
            if height[i] > height[i+1]:
                k = i+1
                p = k
                while height[p] < height[i] and height[i] > height[k]:
                    p += 1
                    if p >= len(height):
                        if height[i] > height[i+1] + 1:
                            height[i] = height[i] - 1
                            p = k
                            continue
                        else:
                            break
                    if height[p] >= height[i]:
                        partsum = max(height[i+1:p])
                        dif = height[i] - partsum
                        onesum = (p-i-1)*(dif)
                        res += onesum
                        height[i] -= dif
                        if height[i] > height[k]:
                            p = k
                        else:
                            p = k + 1

        return res


a = Solution()
print(a.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
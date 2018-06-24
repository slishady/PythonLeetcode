class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        Solution.anslist = []
        self.DFS(candidates, target, 0, [])
        return Solution.anslist

    def DFS(self, candidates, target, start, valuelist):
        if target ==  0:
            return Solution.anslist.append(valuelist)
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                return 
            self.DFS(candidates, target-candidates[i], i, valuelist+[candidates[i]])



a = Solution()
print(a.combinationSum([2,3,6,7], 7))
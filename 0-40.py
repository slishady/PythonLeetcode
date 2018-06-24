class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        Solution.ans_list = []
        candidates.sort()
        self.DFS(candidates, target, 0, [])
        return Solution.ans_list

    def DFS(candidates, target, i, valuelist):
        if target == 0:
            Solution.ans_list.append(valuelist)
        for i in range(i, len(candidates)):
            if candidates[i] > target:
                return
            self.DFS(candidates, target-candidates[i], i+1, valuelist+[candidates[i]])
            
             
            
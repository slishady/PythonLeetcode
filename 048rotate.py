class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        copy = []
        for i in matrix:
            copy.append(list(i))
        dim = len(matrix)
        for i in range(dim):
            for j in range(dim):
                matrix[j][i] = copy[dim-i-1][j]

    
a = Solution()
b = [[1,2,3],[4,5,6],[7,8,9]]
a.rotate(b)
print(b)


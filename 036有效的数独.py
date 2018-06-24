class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        self.center = [(1,1), (1,4), (1,7), (4,1), (4,4), (4,7), (7,1), (7,4), (7,7)]
        # self.range = ["1", "2", "3", "4", "5", "6", "7", "8", "9", '.']
        ans = True
        for i in range(9):
            ans = self.judgelineandrow(board, i)
            if ans is False:
                break

        if ans is False:
            return ans

        ans = self.judgesqure(board)
        return ans

        


    def judgelineandrow(self, board, i):
        rowcount = 0
        colcount = 0
        rowset = set()
        colset = set()
        ans = True
        for j in range(9):
            # if board[j][i] not in self.range or board[i][j] not in self.range:
            #     ans = False
            #     return ans
            if board[i][j] != '.':
                colcount += 1
                colset.add(board[i][j])
            if board[j][i] != '.':
                rowcount += 1
                rowset.add(board[j][i])
        if len(rowset) != rowcount or len(colset) != colcount:
            ans = False
        return ans

    def judgesqure(self, board):
        ans = True
        for i , j in self.center:
            squareset = set()
            numbercount = 0
            for k in range(-1, 2):
                for n in range(-1, 2):
                    if board[i-k][j-n] != '.':
                        numbercount += 1
                        squareset.add(board[i-k][j-n])
            if len(squareset) != numbercount:
                ans = False
                return ans
        return ans
            
print(a.isValidSudoku(L)))
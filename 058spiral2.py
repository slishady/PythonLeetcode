class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix= [[0 for _ in range(n)] for _ in range(n)]
        self.cyc(n, n, 0, 0, 1, matrix, 0)
        return matrix
        


    def cyc(self, row, column, ri, ci, value, matrix, case):
        if row == 0 or column == 0:
            return 
        if case == 0:
            endci = ci + column
            for i in range(ci, endci):
                matrix[ri][i] = value
                value += 1
            row -= 1
            ri = ri + 1
            ci = endci - 1
            case = (case + 1)%4
            self.cyc(row, column, ri, ci , value, matrix, case)

        elif case == 1:
            endri = ri + row
            for i in range(ri, endri):
                matrix[i][ci] = value
                value += 1
            column -= 1
            ri = endri - 1
            ci = ci - 1
            case = (case + 1)%4
            self.cyc(row, column, ri, ci, value, matrix, case)

        elif case == 2:
            endci = ci - column
            for i in range(ci, endci, -1):
                matrix[ri][i] = value
                value += 1

            row -= 1
            ri = ri - 1
            ci = endci + 1
            case = (case+1)%4
            self.cyc(row, column, ri, ci, value, matrix, case)

        elif case == 3:
            endri = ri - row
            for i in range(ri, endri, -1):
                matrix[i][ci] = value
                value += 1
            
            column -= 1
            ri = endri + 1
            ci = ci + 1
            case = (case + 1)%4
            self.cyc(row, column, ri, ci, value, matrix, case)
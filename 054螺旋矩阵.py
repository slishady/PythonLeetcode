class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def cyc(row, column, ri, ci, case):
            if row == 0 or column == 0:
                return
            if case == 0:
                endci = ci + column
                for i in range(ci, endci):
                    re.append(matrix[ri][i])
                row -= 1
                ri += 1
                ci = endci-1
                #我们想让case 不断增加但在0-4内循环
                case = (case + 1)%4
                cyc(row, column, ri, ci, case)

            elif case == 1:
                endri = ri + row
                for i in range(ri, endri):
                    re.append(matrix[i][ci])
                column -= 1
                ci -= 1
                ri = endri-1
                case = (case+1)%4
                cyc(row, column, ri, ci, case)

            elif case == 2:
                endci = ci - column
                for i in range(ci, endci, -1):
                    re.append(matrix[ri][ci])
                row -= 1
                ri = ri - 1
                ci = endci + 1
                case = (case+1)%4
                cyc(row, column, ri, ci, case)

            elif case == 3:
                endri = ri - row
                for i in range(ri, endri, -1):
                    re.append(matrix[i][ci])
                column -= 1
                ri = endri + 1
                ci = ci + 1
                case = (case+1)%4
                cyc(row, column, ri, ci, case)

        re = []
        row = len(matrix)
        if row == 0:
            return []
        column = len(matrix[0])
        cyc(row, column, 0, 0, 0)
        return re
            
                 

a = Solution()
print(a.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
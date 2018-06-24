class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """ 
        final_ans = list(self.queens(n, ()))
        return len(final_ans)




    def queens(self, num, state = ()):  
        for pos in range(num):  
            if not self.conflict(state, pos):  
                #产生当前皇后的位置信息  
                #如果只剩一个皇后没有放置  
                if len(state) == num-1:  
                    yield (pos,)
                #否则，把当前皇后的位置信息，添加到状态列表里，并传递给下一皇后。  
                #程序要从前面的皇后得到包含位置信息的元组（元组不可更改）  
                #并要为后面的皇后提供当前皇后的每一种合法的位置信息  
                #所以把当前皇后的位置信息，添加到状态列表里，并传递给下一皇后。  
                else:  
                    for result in self.queens(num, state+(pos,)):
                        yield (pos, ) + result


    def conflict(self, state, nextX):
        nextY = len(state)
        for i in range(nextY):
            if abs(state[i]-nextX) in (0, nextY-i):
                return True
        return False


a 
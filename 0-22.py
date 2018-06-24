class Solution:  
    # @param an integer  
    # @return a list of string  
    def generateParenthesis(self, n):  
        res = []
        self.generate(n, n, '', res)
        return res

    def generate(self, left, right, s, res):
        if left == 0 and right == 0:
            res.append(s)
        if left > 0:
            self.generate(left - 1, right, s+'(', res)
        if right > left:
            self.generate(left, right - 1, s+')', res)
            

class Solution:  
    # @param an integer  
    # @return a list of string 
    def generateParenthesis(self, n):
        res_list = []
        self.DFS(n, n, '', res)
        return res_list
        

    def DFS(self, left, right, s, res):
        if left == 0 and right == 0:
            res.append(s)
        else:
            if left > 0:
                self.DFS(left-1, right, s+'(', res)
            if right > left:
                self.DFS(left, right-1, s+')', res)
        
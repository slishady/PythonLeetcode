import functools
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #一共能向下走的步数
        down = n-1
        #一共能向右走的步数
        right = m-1
        if m == 1 or n == 1:
            return max(m, n)
        if m > n:
            a = functools.reduce(lambda x, y: x*y, range(m, m+n-1))
            b = functools.reduce(lambda x, y: x*y, range(1, n))
        else:
                
            a = functools.reduce(lambda x, y: x*y, range(n, m+n-1))
            b = functools.reduce(lambda x, y: x*y, range(1, m))
        return a/b 
        
        self.walk(right, down)
        return self.count

    def walk(self, right, down):
        if right == 0 and down == 0:
            self.count += 1
        else:
            if right > 0:
                self.walk(right-1, down)
            if down > right:
                self.walk(right, down-1)

        
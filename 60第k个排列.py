class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.length = n
        part = list(map( lambda x: str(x), list(range(1, n+1))))
        ans = []
        self.DFS(part, "", ans)
        return ans[k-1]
        

    def DFS(self, part, s, ans):
        if len(s) == self.length:
            ans.append(s)
        else:
            for a in part:
                self.DFS(part[:part.index(a)] + part[part.index(a)+1:], s+a, ans)
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        a = "".join(list(map(lambda x: str(x), list(range(1, n+1)))))
        b = [1]
        for i in range(1, n+1):
            b.append(b[i-1]*i)
        k = k % b[n]

        if k == 1:
            return a
        else:
            if k < 2:
                k = b[n]
            for i in range(k-1):
                a = self.Next(a)
            return a



        

    def Next(self, s):
        i = len(s) - 1
        while i - 1>= 0 and s[i] < s[i-1]:
            i = i - 1
        mid = i
        if i - 1 >= 0:
            swap = i - 1
        else:
            swap = i
        i = len(s) - 1
        while i - 1 >= 0 and s[i] < s[swap]:
            i -= 1

        a = list(s)

        a[i], a[swap] = a[swap], a[i]
        a = a[:mid] + sorted(a[mid:])
        return "".join(a)

a = Solution()
print(a.getPermutation(3, 6))
            
class Solution:
    def getPermutation(self, n, k):
        p = [1]
        for i in range(1, n+1):
            p.append(p[i-1]*i)
        digit = list("123456789")
        
        num = n-1
        res = ""
        while num:
            t = (k-1)//p[num]
            k = k - t*p[num]
            res += digit[t]
            digit.remove(digit[t])
            num -= 1
        res += digit[k-1]
        return res

class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        #这个self.fac方便我们通过下标直接读取i的阶乘
        #i! = self.fac[i]
        self.fac = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

        #初始化我们先求n-1的阶乘
        i = n - 1
        #我们可以选择加入结果的数字
        num = list(range(1, n+1))
        #最终结果
        ret = ""
        while i >= 0:
            #a用来获得我们每一次要求的那一位在num里的下标
            #b表示以a下标的数字为头后还剩下多少个排列
            a, b = k // self.fac[i], k % self.fac[i]
            #如果b==0，代表整除干净了，这时候应该是以某一个数字开头的最后一项
            #所以a要回退一位，因为实际上a还没到达目前这个值，它只是以上一个数字开头的最大结果
            if b == 0:
                a -= 1
            
            # 如果a 有效， 我们就把a下标的数字加入结果，并且更新num，避免重复。
            if a >= 0:
                ret += str(num[a])
                del num[a]
                i -= 1
            k = b
            #因为是最大结果，所以我们把剩下的数字全部reverse，再加入，就是以a下标数字开头的最大结果
            if b == 0:
                for i in "".join(reversed(num)):
                    ret += i
                break
        return ret

            

a = Solution()
print(a.getPermutation(3, 3))
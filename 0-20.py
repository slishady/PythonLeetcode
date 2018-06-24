class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftlist = []
        #左括号与右括号，注意相匹配符号的index也是匹配的
        left = '{[('
        right = '}])'
        #因为s全是括号，所以我们直接遍历
        for i in s:
            #是左括号，加进栈结构
            if i in left:
                leftlist.append(i)

            else:
                #遇到右括号，取出最近放入的左括号
                if len(leftlist) != 0:
                    if left.index(leftlist.pop()) != right.index(i):
                        return False
                #取不出，说明有右括号多了
                else:
                    return False
        #当左括号不剩下多的，才true
        if len(leftlist) == 0:
            return True
        #否则false
        else:
            return False


a = Solution()
print(a.isValid("()"))
print(a.isValid("()[]{}"))
print(a.isValid("(]"))
print(a.isValid("([)]"))
print(a.isValid("{[]}"))



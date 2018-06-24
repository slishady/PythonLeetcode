
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        t = head
        tot = 0
        p = t
        if k == 1:
            return head
        while p != None:
            p = p.next
            tot += 1
        cnt = 0
        while t != None:
            if cnt + k <= tot:
                if cnt == 0:
                    head = self.reverse(t, k)
                    cnt += k
                else:
                    i = t.next
                    newhead = self.reverse(i, k)
                    cnt += k
                    t.next = newhead
                    t = i

            else:
                break
        return head
                
                

    def reverse(self, t, k):
        count = 1
        oldhead = t
        while count < k:
            newhead = t.next
            t.next = newhead.next
            newhead.next = oldhead
            oldhead = newhead
            count += 1
        return newhead

L = [1, 2, 3, 4, 5]
head = ListNode(1)
j = head
for i in L[1:]:
    j.next = ListNode(i)
    j = j.next

a = Solution()
def output(p):
    while p != None:
        print(p.val)
        p = p.next


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        #保存头部节点
        t = head
        tot = 0
        p = t
        if k == 1:
            return head
        #用tot算出总节点数，知道什么时候该停止
        while p != None:
            p = p.next
            tot += 1
        #cnt表示目前为止一共reverse了几个节点
        cnt = 0
        #从头部开始遍历
        while t != None:
            #判断翻转K个是否越界
            if cnt + k <= tot:
                #分情况讨论，如果是第一次reverse
                if cnt == 0:
                    head = self.reverse(t, k)
                    cnt += k
                else:
                    #如果不是第一次了
                    #这里有个巧妙的地方，当我们进行完第一次后，t指向第一个reverse区间的最后一个节点
                    i = t.next
                    
                    #通过函数传递一个newhead,用newhead才能改变t.next的值
                    newhead = self.reverse(i, k)
                    #翻转了K个，数量增加K个
                    cnt += k
                    #上个节点的尾部的下一个指向新头
                    t.next = newhead
                    #让t前进，i同样与一开始t一样指向reverse部分最后一个.
                    t = i
            #越界就说明我们已经reverse了能reverse的部分，直接退出
            else:
                break
        return head
                
                

    def reverse(self, t, k):
        #记录目前reverse的数量
        count = 1

        oldhead = t
        while count < k:
            #每次循环都定义一个新头，这个newhead是t 的下一项。
            newhead = t.next
            #把新头从t的下一项删去
            t.next = newhead.next
            #让新头在t的前面
            newhead.next = oldhead
            #新头变成旧头
            oldhead = newhead
            count += 1
        #返回reverse完后最新的头
        return newhead
output(a.reverseKGroup(head, 3))
    



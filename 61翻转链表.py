class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        if head is None:
            return None
        
        #先数链表有几个节点
        i = head
        count = 1
        while i.next is not None:
            i = i.head
            count += 1
        #抛掉重复的转圈
        k = k%count
        if (k == 0) or count == 1:
            return head
        #把链表头尾连起来
        i.next = head

        #从dummy开始运动
        i = dummy
        #运动到新的链表的头的上一个节点
        for _ in range(count - k):
            i = i.next

        j = i.next
        i.next = None
        return j
        
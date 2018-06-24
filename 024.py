# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        t = head
        if t is None:
            return None
        if t.next is None:
            return t
        #先反转第一第二个
        j = t.next
        q = j.next
        j.next = t
        t.next = q
        ans = j


        if t.next is None:
            return ans
        #因为是22翻转，所以应该保证上个节点的后2个节点不为None
        #我们要交换2个节点，最重要的是我们先要定位到这2个节点前面那个节点。
        while t.next.next is not None:
            j = t.next
            q = t.next.next
            j.next = q.next
            t.next = q
            q.next = j
            if t.next is None or t.next.next is None:
                return ans
            t = t.next.next
            if t is None or t.next is None:
                return ans
        return ans
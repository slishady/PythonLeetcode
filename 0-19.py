# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        t = head
        count = 0
        while t != None:
            t = t.next
            count += 1
        order = count - n
        index = 1
        t = head
        while index < order:
            t = t.next
            index+=1
        if order == 0:
            return head.next
        l = t.next
        t.next = l.next
        return head

head = ListNode(1)
head.next = ListNode(2)
a = Solution()
print(a.removeNthFromEnd(head, 2).val)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i = l1
        j = l2
        head = l1
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if j.val < i.val:
            head = j
            while j.next is not None and j.next.val <= i.val:
                j = j.next
            t = j
            j = j.next
            t.next = i
        while i != None and j != None:
            if i.next != None:
                if i.next.val > j.val:
                    t = j
                    j = j.next
                    t.next = i.next
                    i.next = t
                    i = i.next
                else:
                    i = i.next
            else:
                i.next = j
                break
                    

        return head

a = Solution()
l2 = ListNode(1)
l1 = ListNode(5)
l2.next = ListNode(2)
l2.next.next = ListNode(4)

print(l2)
print(a.mergeTwoLists(l1, l2))






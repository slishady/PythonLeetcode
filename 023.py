class Solution:  
    def mergeKLists(self, lists):  
        """ 
        :type lists: List[ListNode] 
        :rtype: ListNode 
        """
        value = []  
        for i in lists:
            t = i
            while t is not None:
                value.append(t.value)
                t = t.next

        value.sort()
        head = ListNode(value[0])
        i = head
        for i in range(1, len(value)):
            i.next = ListNode(value[i])
            i = i.next

        return head

class Solution:  
    def mergeKLists(self, lists):  
        """ 
        :type lists: List[ListNode] 
        :rtype: ListNode 
        """
        value = []
        #遍历所有节点，把他们的值存在列表中  
        for i in lists:
            t = i
            while t is not None:
                value.append(t.val)
                t = t.next
        #对列表排序
        value.sort()
        if len(value) == 0:
            return None
        head = ListNode(value[0])
        j = head
        #把值合并成一个列表
        for i in range(1, len(value)):
            j.next = ListNode(value[i])
            j = j.next

        return head



"""
合并链表
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return []
        
        res = None
        data = []
        asis = None
        for head in lists:
            if not head:
                continue
            if(res == None):
                res = head
            if(asis != None):
                asis.next = head
            while(head != None):
                if(head.next == None):
                    asis = head
                data.append(head.val)
                head = head.next
            
                
        data.sort()
        head = res
        for i in range(len(data)):
            head.val = data[i]
            head = head.next
        return res

"""
两数相加
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        arr1 = str()
        arr2 = str()
        pointer1 = l1
        pointer2 = l2
        while(pointer1 != None):
            arr1 += str(pointer1.val)
            pointer1 = pointer1.next
        
        while(pointer2 != None):
            arr2 += str(pointer2.val)
            pointer2 = pointer2.next
        
        arr3 = str()
        arr4 = str()
        for i in range(len(arr1)):
            arr3 += arr1[len(arr1) - i - 1]
            
        for i in range(len(arr2)):
            arr4 += arr2[len(arr2) - i - 1]
        
        sum = int(arr3) + int(arr4)
        sum = str(sum)
        
        head = None
        for i in range(len(sum)):
            if(i == 0):
                head = ListNode(int(sum[len(sum) - i - 1]))
                pointer = head
            else:
                pointer.next = ListNode(int(sum[len(sum) - i - 1]))
                pointer = pointer.next
        return head

#Reverse List
"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        if(head == None):
            return None
        if(head.next == None):
            return head
        list_head = head
        left = head
        middle = head.next
        right = middle.next
        
        #Check
        if(right == None):
            middle.next = left
            left.next = right
            return middle
        while(right.next != None):
            middle.next = left
            left = middle
            middle = right
            right = right.next
        middle.next = left
        right.next = middle
        list_head.next = None
        return right

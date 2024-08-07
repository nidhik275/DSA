from typing import Optional
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #first = second = third = ListNode()
        curr = head
        prev = next = None
       
        while curr:
            next = curr.next 
            curr.next = prev
            prev = curr
            curr = next
        return prev
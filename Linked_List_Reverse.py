# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#we can solve this problem in 2 way 
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """
        we can  use by 2 pointer 
        currrent and prev 
        time complexity is o(n)
        and memory complexity is o(1)
        but if we do recursive then both of time and 
        """
        prev,curr = None,head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr =nxt
        return prev
        

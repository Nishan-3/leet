# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#floyd's tortoise and here 

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow , fast = head , head # pointing to the initial pointer 

        while fast and fast.next: # this means while fast and fast.next is not null ie it has cycle :
            slow = slow.next  # increasing by 1 

            fast = fast.next.next  #increasing by 2 
            if slow == fast :
                return True 
        return False

        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
            we are given here singly linkedlist 
            here in the general case for a list of length =n the nodes are ordered 
            to be in the following order 

            [0,n-1,1,n-2,2,n-3,3 ......]
            [0,1,2,3,4,5,6]->
            [0,6,2,3,4,5,1]
            [0,6,1,3,4,5,2]

            o(n) ->time 
            and o(1) space 
            if we were using extra memory we could put all of them in 
            extra array and put them in   

        """
        slow,fast = head ,head.next
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        #reverse second half 
        second = slow.next 
        prev=slow.next = None 
        while second:
            tmp = second.next 
            second.next = prev 
            prev = second 
            second = tmp 
        #merge two halves 
        first , second = head ,prev
        while second:
            tmp1,tmp2 = first.next , second.next 
            first.next = second 
            second.next = tmp1 
            first,second = tmp1,tmp2

        

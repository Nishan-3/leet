# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        We are given an array of k linked lists, each sorted in ascending order.
        We must merge all k lists into one sorted linked list and return it.
        Example: [[1,2,4],[1,3,5],[3,6]] → [1,1,2,3,3,4,5,6]
        """

        if not lists or len(lists) == 0:
            return None 

        # Keep merging pairs of lists until only one remains
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))

            lists = mergedLists

        return lists[0]
        
    def mergeList(self, l1, l2):
        """
        Merge two sorted linked lists into a single sorted linked list.
        """
        dummy = ListNode()
        cur = dummy

        # Compare and attach smaller node each time
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        # Attach the remaining nodes
        cur.next = l1 if l1 else l2

        return dummy.next

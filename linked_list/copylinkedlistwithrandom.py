"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #so at first we will create hash map and then we will clone it 
        oldtocopy ={None:None} # we are creating the hash map here 
        cur = head #so initializing the curr var to head of the linked list

        while cur: #first loop for cloning 
            copy = Node(cur.val)
            oldtocopy[cur] = copy
            cur = cur.next 
        cur = head 

        while cur:
            copy = oldtocopy[cur]
            copy.next = oldtocopy[cur.next]
            copy.random = oldtocopy[cur.random]
            cur = cur.next 
        return oldtocopy[head]

        
        

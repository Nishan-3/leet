class ListNode:
    def __init__(self,data,Next = None ):
        self.data = data
        self.Next = None 
        
    def __str__(self):
        return str(self.data)

head = ListNode(1)
a = ListNode(2)
b= ListNode(3)
c = ListNode(4)

head.Next = a
a.Next = b 
b.Next = c
c.Next = None 
print(head)

#here we will reverse the linkedlist with the help of recursion 

def rever(node):
    if node == None :
        return # this is base care for  our 
    
    
    rever(node.Next)
    print(node)
    
rever(head)


    

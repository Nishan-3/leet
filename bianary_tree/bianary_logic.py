class NodeTree:
  def __init__(self,data):
    self.data = data 
    self.left = None 
    self.right = None

  def __str__(self):
    return str(self.data)


head = NodeTree(1)
a = NodeTree(2)
b= NodeTree(3)
c=NodeTree(4)
d = NodeTree(5)
e = NodeTree(6)
f=Nodetree(7)


head.left = a
head.right = b
a.left = c
a.right =d
b.left =e
b.right =f


    
    
  
  

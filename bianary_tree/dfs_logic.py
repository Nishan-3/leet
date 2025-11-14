#here we will make  bianary tree  blueprint 

class Btree:
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None 
        
    def __str__(self):
        return str(self.data)
        
firstnode = Btree(1)
secondnode =Btree(2)
thirdnode = Btree(3)
fouthnode = Btree(4)
fifthnode = Btree(5)

firstnode.left = secondnode
firstnode.right = thirdnode
secondnode.left = fouthnode
secondnode.right =fifthnode



#preorder dfs 
print('pre order')
def preorder(node):
    if node == None:
        return 
    print(node.data)
    preorder(node.left)
    preorder(node.right)
    
preorder(firstnode)


#Inorder dfs
print('inorder dfs')
def inorder(node):
    if node ==None:
        return 
    inorder(node.left)
    print(node.data)
    inorder(node.right)

inorder(firstnode)
print('Post order')
def postorder(node):
    if node == None :
        return 
    postorder(node.left)
    postorder(node.right)
    print(node)
    
postorder(firstnode)

    
    

    
    

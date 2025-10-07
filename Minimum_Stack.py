class MinStack:
    """
    here we will create 2nd stack  as  minstack to solve into time compexity of o(1)
    """
    

    def __init__(self):
        self.stack =[]
        self.minstack =[]#this is the 2nd stack that we created to make the time compexity of o(n)

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val,self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        

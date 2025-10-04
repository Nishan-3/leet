class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        '''
        so this is stack problem 
        last to add and first to out this is stack 
        [1,2,3,4] -> [1,2,3]->[1,2] ->[1]->[]
        so how does the logic works here we will add the 
        element here in an empty array and 
        operators follow operands 
        here is the viusal example 
        [1,2,+,3,*,4,-]
        we will loop through the list 
        our stack will append [1,2]
        now  we will pop out the element as our 3rd index is +
        1+2 ->3 now our new stack will be 
        [3] and apppend 3 -> [3,3,*]
        we will pop 3,3 and multipy it [9]-> [9,4] and [9,4] will be popped out 
        5 

        so how can we solve the problem here we will take one 
        here operators are ['+' ,'-','*','/']
        first we will make an empyt array '''

        stack =[]

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif c =='*':
                stack.append(stack.pop() *stack.pop())
            elif c == "/":
                a,b = stack.pop() , stack.pop() # last and 2nd last element 
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        return stack[0]


            


        

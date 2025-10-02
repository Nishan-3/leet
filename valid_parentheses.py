class Solution:
    def isValid(self, s: str) -> bool:

        '''
        so this is valid parentheses

        parentheses 
        '(' ,')',{}


        here the input string is valid when only 
        every open bracket is closed by the same type of close bracket 
        open brakcets ae closed in the correct order 
        every close bracket has a corresponding open brakcte of the same type 
        stack is last to in first to out .
        ()[]{}"

Push "(" → stack = ["("]

See ")" → matches → pop → stack = []

Push "[" → stack = ["["]

See "]" → matches → pop → stack = []

Push "{" → stack = ["{"]

See "}" → matches → pop → stack = [] 
        '''
        stack =[]
        closetoOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closetoOpen:
                if stack and stack[-1] == closetoOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

    
        

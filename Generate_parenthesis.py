class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        """
        we are given an integer n 
        we have ti return all well-formed parentheses strings 
        that we can generate with n pairs of parentheses .

        only add open paranthesis if open<n
        only add a closing paranthesis if closed<open 
        valid IIF open == closed == n 

        

        """
        stack =[]
        res =[] # which will hold valid parenthesis 

        def backtrack(openN,closedN):
            if openN == closedN ==n:
                res.append("".join(stack))
                return 
            if openN < n:
                stack.append('(')
                backtrack(openN+1,closedN)
                stack.pop()
            if closedN < openN:
                stack.append(')')
                backtrack(openN,closedN+1)
                stack.pop()
        backtrack(0,0)
        return res

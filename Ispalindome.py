class Solution:
    def isPalindrome(self, s: str) -> bool:

        """
        so lets understand this is 2 pointer program 
        what is palindrome 
        it is string that reads the same forward and backward . it is also case sensitive 
        so our constrains is 
        ->time and space complexity . 
        0(n) time and o(1) space 

        here we are given the input of the string s 
        here we should join all of the together like the space also 

        here we are using left and right pointer 

        l and r 
        left from beginning and r from last 
        we increment the left and decrement the right 
        when to stop the loop when l>r . 

        while left not alpha numberica l++ 
        and while right not alfa r--
        also  we will create the new function  alphanum 
        """
        '''l,r = 0,len(s)-1

        while l<r:
            #inpython if we want to call the function inside the object we have to call self
            while l <r and not self.alphanum(s[l]):
                l += 1
            while r>l and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower:
                return false
            l ,r  = l+1 , r-1
        return True 
        

        def alphanum(self,c):
            return(ord('A') <= ord(c) <= ord('Z')or
                ord('a') <= ord(c) <= ord('z')or
                ord('0') <= ord(c) <= ord('9'))
            #this is function to check if the c is alphanum or not , we will return the true ,
            '''
        
        l, r = 0, len(s) - 1

        while l < r:
            # move left pointer until alphanumeric
            while l < r and not self.alphanum(s[l]):
                l += 1
            # move right pointer until alphanumeric
            while r > l and not self.alphanum(s[r]):
                r -= 1

            # compare ignoring case
            if s[l].lower() != s[r].lower():
                return False

            l, r = l + 1, r - 1

        return True

    def alphanum(self, c: str) -> bool:
        # check if c is alphanumeric (without using isalnum)
        return (
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')
        )


        

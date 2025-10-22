class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """
        here the given a sting s , we have to find the longest substring without d
        duplicate characters

        here input is 

        "zxyzxyz"

        here we are using the set for checking the duplicates 
        """
        CharSet = set()
        l,r = 0,1
        res = 0 

        for r in range(len(s)):
            while s[r] in CharSet:  # if duplicate update .
                CharSet.remove(s[l])
                l+= 1 
            CharSet.add(s[r])
            res = max(res,r-l+1)
        return res 



        
        

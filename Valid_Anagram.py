class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        here we can sort but the time and space compexity is n(log(n))
        we want to find in 0(n) 

        so here we wont sort but we can sort this . 
         
         here we have atmost 26 arrays . 

         this can be solved wiht hasmap. 
         mapping the character of count 

         ord() is ascii value 
         here lets take an example the ascii value of a is 80 
         and ascii value of b   is 81 

         so ord(b) - ord(a)  = 1

         here new knowledge to learn so here in  python  we can't use list as the key in dict because its mutable 
        """

        res  = defaultdict(list) #Mapping the charCount toi list of anagrams

        for s in strs:
            count = [0]*26 

            for c in s :
                count[ord(c)-ord("s")] +=1
            res[tuple(count)].append(s)
        
        returnlist(res.values())
        

class Solution:

    def encode(self, strs: List[str]) -> str:

        """
        probably we should make hash map out here 
        encode and decode the string . 
        its kind of tricky question for me 
        i remember my cousin trying to say something about this problem 
        last semester 
        so first i would like to encode it . 
        simple trick i am using ord() method . 
        """
        res =''
        for s in strs:
            res += str(len(s)) +"#"+ s
        return res


    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res


        
        
            


            




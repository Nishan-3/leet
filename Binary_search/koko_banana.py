class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        here we are given an integer array piles 
        piles[i] is the number of bananas in the ith pile 
        we are given integer h which represents number of hours we hvae to eat all of the bananas .
        k-> output 

        here h is always greater than the number of pile . 
        len(p)<= h 

        """

        l,r = 1,max(piles)
        res =r

        while l<=r:
            k=(l+r)//2
            hours =0
            for p in piles:
                hours += math.ceil(p/k)

            if hours<=h:
                res = min(res,k)
                r=k-1
            else:
                l=k+1
        return res

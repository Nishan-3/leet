class Solution:
    def maxArea(self, heights: List[int]) -> int:

        """
        so here they have given the the height 
        so what we can do is we can find the lenght 
        i believe we can compare it using the dummy variable but we are 
        area = l*b
        l ,r 
        height[i or r ] *  len(r-l) 
        Input: height = [1,7,2,5,4,7,3,6]
                        {0,1,2,3,4,5,6,7}

                        here we will do 2 pointer thing 
                        so first we will find 
                        here what is logic 
                        first we will while loop until the lefpointer is less than right 
                        """
        l,r = 0,len(heights)-1
        res = 0 
        while l < r :
            area = min(heights[l],heights[r])* (r-l) # this is the logic to compute the area . len into breadth 
            res = max(res,area)

            if heights[l]<heights[r]:
                l += 1
            else:
                r -=1
            
        return res
    

        

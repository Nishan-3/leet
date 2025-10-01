class Solution:
    def trap(self, height: List[int]) -> int:
        """
        here we are given array of non-negative integers height which represent an eleevation map 

        o(1) solution with  2 pointers 

        here inputs are 

        height =[0,2,0,3,1,0,1,3,2,1]

        here end points cant trap the water ,



        """

        if not height: return 0

        l,r = 0 ,len(height)-1
        leftMax,rightMax = height[l],height[r]
        res = 0 

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax,height[l])
                res += leftMax-height[l]
            else:
                r -=1
                rightMax = max(rightMax,height[r])
                res += rightMax - height[r]
        return res

             

        

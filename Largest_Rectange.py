class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        here we are given an arya of integers with heigths where heights[i] represetns the height 
        of a bar . the width of each bar is 1 

        so we have to retun the largest area of rectange that can be formed among the  bars . 

        here we have to find the solution with o(n) time and o(n) space compexity  

        first condition -> 
        len *heights[i] = area -> maxarea

        """
        maxArea = 0 
        stack =[] #pair (index, height)

        for i , h in enumerate(heights):
            start = i 
            while stack and stack[-1][1] > h:
                index , height = stack.pop()
                maxArea = max(maxArea,height*(i-index))
                start = index 
            stack.append((start,h))

        for i , h in stack:
            maxArea  = max(maxArea , h*(len(heights)-i))
        return maxArea 

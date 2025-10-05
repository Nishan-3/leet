class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #monotonic decreasing stack . 
        """
        here we are given an array of integer temperatures where temperature[i]
        represent the daily temperature of the ith day 
         
        we have to return an array result where result[i] is the number of days after
        the ith day before a warmer temperateure appears on the future days . 

        if there is no day in the future where a warmer temperature will appear for the 
        ith day , set result[i] to 0 intead 

        here we will give the visual example 

        our temperature is [30,38,30,36,35,40,28]

            so here is the logic 
            here we will have two variable 
            one stack which will be an empty array 
            the next will be output also an array 


        """

        res = [0]*len(temperatures)
        stack =[] #pair :[temp,index]

        for i ,t in enumerate(temperatures ):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i-stackInd)
            stack.append([t,i])
        return res 
        

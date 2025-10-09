class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        we are here given m*n 2-d integer array matrix and an integer . target 
        each row in matix is non decreasing order 
        the first integer of every row is greater that the last integer of prev row . 

        we can say this as double bianary seach 
        here the code that len(metrix) for that row might be confusing 
        actually we have 3 rows in the input that is equivalent to lenght of matrix in this 2d 
        array 

        also here we hvae 4 cols so the length of the first row / array[0] will be our column 

        """
        Rows , Cols = len(matrix), len(matrix[0])

        top, bot = 0,Rows-1
        while top <= bot:
            c_row =(top+bot)//2
            if target > matrix[c_row][-1]:
                # [-1] because  we are checking it to last element 
                top = c_row+1
            elif target<matrix[c_row][0]:
                bot = c_row-1
            else:break 
        
        if not(top<= bot):
            return False
        c_row = (top+bot)//2
        l,r = 0,Cols-1

        while l<=r:
            m=(l+r)//2
            if target >matrix[c_row][m]:
                l= m+1
            elif target < matrix[c_row][m]:
                r = m-1
            else:
                return True
        return False
    




        

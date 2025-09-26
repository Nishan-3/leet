class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        """
        we are given 9*9 sudoku board . A soduku board is valid if the followig rules are followed :

        each row must contain the digits 1-9 without duplicates 

        each row must contain the digit 1-9 without duplicates 

        each of the nine 3*3 sub- boxes of the grid must contain the digits 1-9 without the duplicates 

        so return true is soduku is valid otherwise retutn false . 

        |1|2| |
        |4| | |
        | |9|8|
        
        so out time and space complexity is 0(n^2)

        so lets solve this 
        """

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares  = collections.defaultdict(set) # key = (r/3 , c/3)


        #heere we are doing this because we have 9*9 elements also that we are looping though the row and colums 
        for r in range(9):
            for c in range(9):
                #how we made logic if the current row and column is empty then we will continue though the loop 
                
                if board[r][c] == ".":
                    continue 
                    #here we are checking  if the duplicates are there in the  rows of 9*9 
                    #also in the columns and squares .  if there is duplicate then we return the false . 
                if(board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)] ):
                    return False 
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])

        return True 

















        

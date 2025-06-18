class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Cols set
        #rows set
        #squares set

        #for i in range 9:
            #for c in range 9:
                #if board[r][c] == "."
                    #continue
                #if Board in rows or cols or squares
                    #return false
                #populate all sets
        #return true


        columns = collections.defaultdict(set)
        rows =  collections.defaultdict(set)
        squareSection = collections.defaultdict(set) #key = (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if(board[r][c] in rows[r] or 
                board[r][c] in columns[c] or 
                board[r][c] in squareSection[(r//3, c//3)] ):# breaks up squares into 9 sub sections 0 1 2 for rows and columns
                    return False
                columns[c].add(board[r][c])
                rows[r].add(board[r][c])
                squareSection[(r//3, c//3)].add(board[r][c])
        return True

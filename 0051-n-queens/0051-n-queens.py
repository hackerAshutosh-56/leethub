class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        cols=set()
        diag1=set()
        diag2=set()
        def backtrack(row,board):
            if row==n:
                ans.append(board[:])
                return 
            for col in range(n): 
                if col in cols:
                    continue
                if row-col in diag1:
                    continue
                if row+col in diag2:
                    continue

                board.append("."*col+"Q"+"."*(n-col-1))
                cols.add(col)
                diag1.add(row-col)
                diag2.add(row+col)

                backtrack(row+1,board)
                board.pop()

                cols.remove(col)
                diag1.remove(row-col)
                diag2.remove(row+col)
        backtrack(0,[])
        return ans     


        
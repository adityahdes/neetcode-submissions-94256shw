class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{"."} for _ in range(9)]
        cols = [{"."} for _ in range(9)]
        subs = [{"."} for _ in range(9)]
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                k = (int(i / 3)*3) + int((j / 3))
                if(val == "."):
                    continue
                if (val in rows[i] 
                or val in cols[j]
                or val in subs[k]):
                    return False
                rows[i].add(val)
                cols[j].add(val)
                subs[k].add(val)
        return True
        
    
        
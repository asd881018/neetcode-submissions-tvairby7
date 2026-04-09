class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        # directions = horizontally or vertically
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            # out of bound, board[r][c] != word[i]
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or board[r][c] != word[i] or (r, c) in path:
                return False

            i += 1
            path.add((r, c))
            # run dfs in diff directions
            res = (dfs(r + 1, c, i) or 
                   dfs(r - 1, c, i) or 
                   dfs(r, c + 1, i) or 
                   dfs(r, c - 1, i))
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # 1. 
        # iterate each cell, run dfs(), check if it can reach to pac or atl, and curHeight < prevHeight
        # O((m*n)^2)

        # 2. Reverse
        # iterate from Pacfic and Atlantic
        # curHeight >= prevHeight

        # 2 hashset, record where we are able to visit

        # find the node in both hashset, append the node to res[]

        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or 
            c < 0 or r < 0 or c == COLS or r == ROWS or 
            heights[r][c] < prevHeight):
                return

            visit.add((r, c))

            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res



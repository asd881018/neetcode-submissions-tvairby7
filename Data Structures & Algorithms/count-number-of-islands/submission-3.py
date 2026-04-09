class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visit = set()
        rows, cols = len(grid), len(grid[0])
        res = 0

        def bfs(r, c):
            q = collections.deque() # store neighbors
            visit.add((r, c))
            q.append((r, c))

            while q:
                r, c = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    newR = r + dr
                    newC = c + dc

                    if newR in range(rows) and newC in range(cols) and grid[newR][newC] == "1" and (newR, newC) not in visit:
                        q.append((newR, newC))
                        visit.add((newR, newC))

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and grid[r][c] == "1":
                    bfs(r, c)
                    res += 1
                    
        return res
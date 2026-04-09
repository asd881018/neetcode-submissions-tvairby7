class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # tree does not include cycle, every node need to be connected to one graph

        # n = 5
        # edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
        # 0 <-> 1 <-> 4
        #   <-> 2
        #   <-> 3

        # check if len of visit == n to prevent edge cases: 0 <-> 1, 2 <-> 3

        visit = set()

        # hashmap for storing neigbors by edges, {0:[1,2,3], 1:[0,4]...}
        neigbors = {i:[] for i in range(n)}
        
        for n1, n2 in edges:
            neigbors[n1].append(n2)
            neigbors[n2].append(n1)

        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)

            for j in neigbors[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False

            return True

        return dfs(0, -1) and n == len(visit)

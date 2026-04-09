class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # has no cycle, and nodes are connect in one graph

        # 0 <-> 1 <-> 2 <-> 3
        #   <-> 4

        # edge case: 0 <-> 1, 2 <-> 3

        visit = set()
        # {0:[1,4], 1:[2]...}
        nodeMap = {i:[] for i in range(n)}
        
        for node1, node2 in edges:
            nodeMap[node1].append(node2)
            nodeMap[node2].append(node1)

        def dfs(cur, prev):

            if cur in visit:
                return False

            visit.add(cur)
            
            for node in nodeMap[cur]:
                if node == prev:
                    continue
                if not dfs(node, cur):
                    return False

            return True

        return dfs(0, -1) and n == len(visit)
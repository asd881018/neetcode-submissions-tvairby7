class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # 0 -> 1 -> 2 -> 3
        #   -> 4

        # prerequisites = [[1,0],[2,1],[3,2],[4,0]]
        # numCourses = 5

        # preMap = {0:[1,4], 1:[2]..., 3:[]}
        # visit = set() -> if we visited the node alr, return False (cycle)

        preMap = {}
        visit = set()

        for i in range(numCourses):
            preMap[i] = []

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(cur):
            # base case
            if cur in visit: # -> has cycle
                return False
            if preMap[cur] == []: # no prerequisite
                return True
            
            visit.add(cur)
            for crs in preMap[cur]:
                if not dfs(crs):
                    return False
            visit.remove(cur)

            return True

        # 1->2, 3->4, in case there's not link for course 3
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
        

            


        
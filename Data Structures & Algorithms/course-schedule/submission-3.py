class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 0 -> 1 -> 2 -> 3
        #   -> 4

        visit = set() # check cycle
        # {0: [1,4], 1: [2]...}

        preMap = {i:[] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            preMap[course].append(prerequisite)

        def dfs(i):
            if i in visit:
                return False

            if preMap[i] == []:
                return True

            
            visit.add(i)
            for j in preMap[i]:
                if not dfs(j):
                    return False
            visit.remove(i)
            preMap[i] = []

            return True

        # 0 -> 1, 3 -> 4
        # loop the numCourses at the end

        for n in range(numCourses):
            if not dfs(n):
                return False
        return True
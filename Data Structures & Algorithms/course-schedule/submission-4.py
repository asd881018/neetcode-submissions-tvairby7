class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 0 -> 1 -> 2 -> 3
        #   -> 4

        
        # 0 <-> 1 edge case: include cycle
        visit = set()

        # {0:[], 1:[], ...}
        preMap = {i:[] for i in range(numCourses)}

        # {0:[1, 4]}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        def dfs(course):
            if course in visit:
                return False
            if preMap[course] == []:
                return True

            visit.add(course)

            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False

            preMap[course] == []
            visit.remove(course)
            
            return True



        
        # edge case: 0 -> 1 and 2-> 3, no connection of 1 and 2
        for n in range(numCourses):
            if not dfs(n):
                return False
        
        return True

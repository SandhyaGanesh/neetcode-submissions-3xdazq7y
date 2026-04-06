class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList =[[] for _ in range(numCourses)]
        for prereq in prerequisites:
            c = prereq[0]
            p = prereq[1]
            adjList[c].append(p)
        
        res = True

        def dfs(course, visited):
            nonlocal res
            if course in visited:
                res = False
                return
            visited.add(course)
            for prereq in adjList[course]:
                dfs(prereq, visited)
            visited.remove(course)
        
        for course in range(numCourses):
            visited = set()
            dfs(course, visited)
        
        return res
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for course, prereq in prerequisites:
            indegree[course] += 1
            adjList[prereq].append(course)
        
        q = deque([])
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        
        order = []
        while q:
            course = q.popleft()
            order.append(course)
            for dependantCourse in adjList[course]:
                indegree[dependantCourse] -= 1
                if indegree[dependantCourse] == 0:
                    q.append(dependantCourse)

        if len(order) == numCourses:
            return order
        else:
            return []

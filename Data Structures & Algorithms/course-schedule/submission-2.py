class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph
        courses = [[] for _ in range(numCourses)]
        # build indegree array
        indegree = [0] * numCourses
        for a, b in prerequisites:
            courses[b].append(a)
            indegree[a] += 1

        def dfs(idx):
            if idx in visited:
                return

            visited.add(idx)
            for i in range(len(courses[idx])):
                c = courses[idx][i]
                indegree[c] -= 1
                if indegree[c] == 0:
                    dfs(c)

            return
        
        # check cycle
        visited = set()
        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)

        
        if len(visited) != numCourses:
            return False
        return True
        
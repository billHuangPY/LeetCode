class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if len(prerequisites) == 0 or prerequisites == None:
            return True

        ## Create Adjacent List first
        adj = [[] for i in range(numCourses)]
        for edge in prerequisites:
            adj[edge[1]].append(edge[0])

        ## Create visited list, where 0: unvisited, 1: visited, -1: visiting. Cycle only appear when the traversal meet a visiting node.
        visited = [0 for i in range(numCourses)]

        for i in range(numCourses):
            if visited[i] == 0:
                if not self.dfs(adj, visited, i):
                    return False

        return True

    def dfs(self, adj, visited, index):
        if visited[index] == -1:
            return False

        if visited[index] == 1:
            return True

        ## only the Same DFS path shared -1, once having branch visited turned to 1
        visited[index] = -1
        for i in adj[index]:
            if not self.dfs(adj, visited, i):
                return False

        visited[index] = 1
        return True

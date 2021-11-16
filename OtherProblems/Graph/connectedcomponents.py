class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[][] int
        :rtype: int
        """
        ## Create Adjacent List
        adj = [[] for i in n]

        for edge in edges:
            node1, node2 = edge[0], edge[1]
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        ## Create Visited List
        visited = [False for i in n]

        count = 0
        for i in n:
            if not visited[i]:
                count += 1
                self.dfs()
        
        return count
    
    
    def dfs(self, adj, visited, i):
        visited[i] = True

        for node in adj[i]:
            if not visited[node]:
                self.dfs(adj, visited, node)
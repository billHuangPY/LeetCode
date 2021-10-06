class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        ## Create Adjacent List
        adj = [[] for i in range(n)]
        for edge in dislikes:
            node1, node2 = edge[0]-1, edge[1]-1
            adj[node1].append(node2)
            adj[node2].append(node1)

        ## groups: unvisited -0, group1 - 1, group2 - -1
        groups = [0 for i in range(n)]

        for i in range(n):
            if groups[i] == 0 and not self.dfs(adj, i, 1, groups):
                return False
        
        return True
    
    def dfs(self, adj, index, group, groups):
        groups[index] = group

        ## j are the neighbor nodes of index
        for j in adj[index]:
            ## if the group of j is the same as index, return false
            if groups[j] == group:
                return False
            ## if j hasn't labeled, but after labeled by dfs, found out false of the traversal, return false
            if groups[j] == 0 and not self.dfs(adj, j, -group, groups):
                return False

        return True


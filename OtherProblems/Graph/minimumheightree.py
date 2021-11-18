class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1 or edges == None or len(edges) == 0:
            return [0]

        ## Set up the adjacency list
        adj = [[] for i in range(n)]
        for edge in edges:
            node1, node2 = edge[0], edge[1]
            adj[node1].append(node2)
            adj[node2].append(node1)

        ## Find the leaves where the node only has 1 of the adjacency list length
        leaves = []
        for i in range(n):
            if len(adj[i]) == 1:
                leaves.append(i)

        ## The Possible root could be one or two
        while n > 2:
            new_leaves = []
            n -= len(leaves)

            ## Find the correspond node near the leaves and remove the leaves from their adjacency list
            for i in leaves:
                j = adj[i]
                adj[j].remove(i)
                ## Find if the correspond node became a leaf
                if len(adj[j]) == 1:
                    new_leaves.append(j)

            leaves = new_leaves

        return leaves

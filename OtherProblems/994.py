class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        k = len(grid[0])
        
        node_value = []
        edges = []
        rotten = []
        node_num = len(grid)*k
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                edges.append([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                node_value.append(grid[i][j])
                if grid[i][j] <= 0:
                    node_num -= 1
                    continue
                elif grid[i][j] == 2:
                    rotten.append(i*k+j)
                if i > 0 and grid[i-1][j] > 0:
                    edges[i*k+j].append((i-1)*k+j)
                if j > 0 and grid[i][j-1] > 0:
                    edges[i*k+j].append(i*k+j-1)
                if i < len(grid)-1 and grid[i+1][j] > 0:
                    edges[i*k+j].append((i+1)*k+j)
                if j < k-1 and grid[i][j+1] > 0:
                    edges[i*k+j].append(i*k+j+1)
        
        visited, pre_visited_num = set(rotten), len(rotten)
        times = -1
        while (times > 0 and not pre_visited_num == len(visited)) or times <= 0:
            pre_visited_num = len(visited)
            round_rotten = set()
            for node in rotten:
                visited.add(node)
                for adj in edges[node]:
                    if not adj in visited and not adj in round_rotten:
                        round_rotten.add(adj)
            rotten = round_rotten
            times += 1
            
        return -1 if not len(visited) == node_num else times-1
        
                    
                
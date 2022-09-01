class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ans = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                grid[i][j] = '0'
                ans += 1
                queue = [(i,j)]
                while len(queue) > 0:
                    (x, y) = queue[0]
                    del queue[0]
                    if x - 1 >= 0 and grid[x-1][y] == '1':
                        grid[x-1][y] = '0'
                        queue.append((x-1,y))
                    if y - 1 >= 0 and grid[x][y-1] == '1':
                        grid[x][y-1] = '0'
                        queue.append((x, y-1))
                    if x + 1 < m and grid[x+1][y] == '1':
                        grid[x+1][y] = '0'
                        queue.append((x+1, y))
                    if y + 1 < n and grid[x][y+1] == '1':
                        grid[x][y+1] = '0'
                        queue.append((x, y+1))
        return ans
'''
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(grid, i, j):
            if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)
            return
    
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                ans += 1
                dfs(grid, i, j)
        return ans
'''
class Solution(object):
    m = 0
    n = 0

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.m = len(grid[0])
        self.n = len(grid)

        count = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[j][i] == '1':
                    count += 1
                    self.fliptozero(grid, i, j, 1)
        return count
        
    def fliptozero(self, grid, x, y, dir):
        if(x < 0 or y < 0 or x >= self.m or y >= self.n or grid[y][x] == '0'):
            return
        
        grid[y][x] = '0'

        if (dir != 0):
            self.fliptozero(grid, x-1, y, 2)
        if (dir != 1):
            self.fliptozero(grid, x, y-1, 3)
        if (dir != 2):
            self.fliptozero(grid, x+1, y, 0)
        if (dir != 3):
            self.fliptozero(grid, x, y+1, 1)
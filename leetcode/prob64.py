"""
最小路径和
"""
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m = len(grid)
        n = len(grid[0])
        value = [([0]*n) for i in range(m)]
        value[0][0] = grid[0][0]
        
        
        for i in range(1,m):
            value[i][0] = grid[i][0] + value[i-1][0]
        for i in range(1,n):
            value[0][i] = grid[0][i] + value[0][i-1]
            
        for i in range(1,m):
            for j in range(1,n):
                value[i][j] = min(value[i-1][j], value[i][j-1]) + grid[i][j]
        return value[m-1][n-1]

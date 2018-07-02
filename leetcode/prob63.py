class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        
        step = [([0]*n) for i in range(m)]
        
        if(obstacleGrid[0][0] == 1):
            return 0
        else:
            step[0][0] = 1
        
        for i in range(1,m):
            if(obstacleGrid[i][0] != 1 and step[i-1][0] != 0):
                step[i][0] = 1
            else:
                step[i][0] = 0
        for i in range(1,n):
            if(obstacleGrid[0][i] != 1 and step[0][i-1] != 0):
                step[0][i] = 1
            else:
                step[0][i] = 0
            
        for i in range(1,m):
            for j in range(1,n):
                if(obstacleGrid[i][j] == 1):
                    step[i][j] = 0
                else:
                    step[i][j] = step[i-1][j] + step[i][j-1]
        
        return step[m-1][n-1]

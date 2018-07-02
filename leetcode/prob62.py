class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        
        Step = [([0]*n) for i in range(m)]

        for i in range(m):
            Step[i][0] = 1
        
        for i in range(n):
            Step[0][i] = 1
        
        
        for i in range(1,m):
            for j in range(1,n):
                Step[i][j] = Step[i-1][j] + Step[i][j-1]
        
        return Step[m-1][n-1]

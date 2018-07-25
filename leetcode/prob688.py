class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        
        moves=(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),

        #curr=[[0]*(N+2) for _ in xrange(N+2)]
        curr = [[0]*N for _ in range(N)]
        for i in xrange(N):
            for j in xrange(N):
                curr[i][j]=1

        for k in xrange(K):
            #next=[[0]*(N+2) for _ in xrange(N+2)]
            next = [[0]*N for _ in range(N)]
            for i in xrange(N):
                for j in xrange(N):
                    for m in moves:
                        I,J=i+m[0],j+m[1]
                        if(I<0 or I>=N or J<0 or J>=N):
                            next[i][j] += 0
                        else:
                            next[i][j]+=curr[I][J]
            curr=next

        return 1.0*curr[r][c]/pow(8,K)

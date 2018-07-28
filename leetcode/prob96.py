"""
这个题需要用到卡特兰数，即N个节点组成的二叉树有多少种形态。
https://blog.csdn.net/xiaomimi3456/article/details/52590220
每种形态里，必有一种是符合二叉搜索数的，即左孩子比父节点小，右孩子比父节点大。
"""
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0]*(n + 1)
        nums[0] = 1
        
        for i in range(1,n+1):
            temp = 0
            for j in range(1,i+1):
                temp += nums[j-1]*nums[i-j]
                
            nums[i] = temp
            
        return nums[n]

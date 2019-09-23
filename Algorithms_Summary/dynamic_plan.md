# Algorithms Summary--Dynamic Plan

### 1. 序列类型的动态规划（一维数组）
* 跳台阶的可能次数
* 使用最小花费爬楼梯

<pre><code>
# Example: leetcode 746
class Solution(object):
    def minCostClimbingStairs(self, cost):
        if(len(cost) == 0):
            return None
        if(len(cost) == 1):
            return cost[0]
        
        cost_len = len(cost)
        res = [0]*(cost_len+1)
        res[0] = cost[0]
        res[1] = cost[1]
        temp = cost
        temp.append(0)
        for i in range(2, cost_len+1):
            res[i] = min(res[i-1]+temp[i], res[i-2]+temp[i])
        
        return res[-1]
</code></pre>
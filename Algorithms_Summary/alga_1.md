# Algorithms Summary

### 1. 获取某些特定值倍数的有序数列
* 丑数（只包含2,3,5质因子的数[1,2,3,4,5,6,8,9,10...], **特例是1，也属于丑数**）

#### Solution：三指针
<pre></code>
class Solution(object):
    def nthUglyNumber(self, n):
        if not n:
            return None
        # define the return list
        res = [0] * n
        res[0] = 1
        # define 3 pointers
        p1 = p2 = p3 = 0
        for i in range(1, n):
            res[i]  = min(2*res[p1], 3*res[p2], 5*res[p3])
            if(res[i] >= 2*res[p1]):
                p1 += 1
            if(res[i] >= 3*res[p2]):
                p2 += 1
            if(res[i] >= 5*res[p3]):
                p3 += 1
                
        return res[-1]
</code></pre>
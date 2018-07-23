class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        leftMax = [0 for i in range(len(height))]
        rightMax = [0 for i in range(len(height))]
        curMax = 0
        rainSum = 0
        
        for i in range(len(height)):
            leftMax[i] = curMax
            curMax = max(curMax, height[i])
            
        curMax = 0
        
        for i in range(len(height)-1,-1,-1):
            rightMax[i] = curMax
            curMax = max(curMax, height[i])
            
        for i in range(len(height)):
            if(leftMax[i] != 0 and rightMax[i] != 0):
                temp = min(leftMax[i], rightMax[i])
                
                temp = temp - height[i]
                if(temp > 0):
                    rainSum += temp
        return rainSum

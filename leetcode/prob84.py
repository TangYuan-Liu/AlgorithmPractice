"""
柱状图中最大矩形
"""

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        if not heights:
            return 0
 
        stack = []
        square = 0
        
        for i in range(len(heights)):
            if(len(stack) == 0):
                stack.append(heights[i])
            else:
                count = 0
                if(heights[i] >= stack[-1]):
                    stack.append(heights[i])
                else:
                    while(len(stack) >0 and stack[-1] > heights[i]):
                        temp = stack.pop()
                        count += 1
                        square = max(square, count * temp)
                    for j in range(count+1):
                        stack.append(heights[i])
        count = 0
        while(len(stack) != 0):
            count += 1
            temp = stack.pop()
            square = max(square, temp*count)
            
        
        return max(square, max(heights))

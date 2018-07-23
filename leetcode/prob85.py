class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        res = 0
        temp = [0 for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            if(i == 0):
                for j in range(len(matrix[i])):
                    temp[j] = int(matrix[i][j])
            else:
                for j in range(len(matrix[i])):
                    if(matrix[i][j] == '0'):
                        temp[j] = 0
                    else:
                        temp[j] += int(matrix[i][j])
            res = max(res, self.findMax(temp))
                
        return res
    
    def findMax(self, heights):
            
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

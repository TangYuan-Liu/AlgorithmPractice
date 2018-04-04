"""
Search a 2D Matrix
"""

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        
        def scan(matrix, target):
            length = len(matrix)
            start = 0
            end = length 
            middle = length / 2
            while(middle != start and middle != end):
                if matrix[middle] == target:
                    return True
                if(matrix[middle] > target):
                    end = middle
                    middle = start + (middle - start) / 2
                    continue
                else:
                    start = middle
                    middle = middle + (end - middle) / 2
                    continue
            if(matrix[middle] == target):
                return True
            else:
                return False
            
            
            """
            for i in range(len(matrix)):
                if(matrix[i] == target):
                    return True
            return False
            """
    
        rows = len(matrix)
        start = 0
        end = rows 
        middle = rows / 2
        if(rows == 0):
            return False
        
        while(middle != start and middle != end):
            if(matrix[middle][0] == target or matrix[middle][-1] == target):
                return True
            if(matrix[middle][-1] > target):
                if(matrix[middle][0] < target):
                    return(scan(matrix[middle], target))
                else:
                    end = middle
                    middle = start + (middle - start) / 2
                    continue
            else:
                start = middle
                middle = middle + (end - middle) / 2
                continue
        
        return scan(matrix[middle], target)        
                    

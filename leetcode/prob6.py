"""
Z型输出字符串
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        out = numRows * ['']
        
        index = 0
        step = 0
        
        if(numRows >= len(s) or numRows == 1):
            return s
        
        for alp in s:
            out[index] += alp
            if(index == 0):
                step = 1
            else:
                if(index == numRows-1):
                    step = -1
            index += step
            
        return ''.join(out)

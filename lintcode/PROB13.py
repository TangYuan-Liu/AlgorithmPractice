"""
strStr
"""

class Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """
    def strStr(self, source, target):
        # write your code here
        if(source == None or target == None):
            return -1
        if(len(source) < len(target)):
            return -1
        
        if(source == '' and target == ''):
            return 0
        
        if(target == '' and source != ''):
            return 0
        
        for i in range(len(source)):
            if(source[i] == target[0]):
                if((len(source) - i) < len(target)):
                    continue
                else:
                    if(source[i:i+len(target)] == target):
                        return i
                    else:
                        continue
        return -1
        

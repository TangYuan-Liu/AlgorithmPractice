"""
Rotate String
"""

class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        # write your code here
        """
        help = str[-offset:]
        length = len(str)
        str = (help + str)[0:length]
        """
        length = len(str)
        if(length > 0):
            offset = offset % length
        
        new_str = (str + str)[(length - offset):(2*length-offset)]
        
        for i in range(length):
            str[i] = new_str[i]
            

#翻转整数
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = str(x)
        out = str()
        if(temp[0] == '-'):
            out += '-'
            temp = temp[1:]
        for i in range(len(temp)):
            out += temp[len(temp)-i-1]
            
        out = int(out)
        
        if(out < (-2**31) or out > (2**31 - 1)):
            return 0
        else:
            return out 

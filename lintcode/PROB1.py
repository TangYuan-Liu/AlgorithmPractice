"""
A+B problems
"""

class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        # write your code
        if a == b:
            return a << 1
        if a == -b:
            return 0
        while(b != 0):
            sum_1 = a ^ b
            sum_2 = (a & b) << 1
            a = sum_1
            b = sum_2
        return a

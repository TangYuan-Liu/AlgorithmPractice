"""
Fizz Buzz
"""

class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        # write your code here
        my_list = []
        for i in range(n):
            x = (i + 1) % 3
            y = (i + 1) % 5
            if((x == 0) and (y == 0)):
                my_list.append('fizz buzz')
            if((x == 0) and (y != 0)):
                my_list.append('fizz')
            if((x != 0) and (y == 0)):
                my_list.append('buzz')
            if((x != 0) and (y != 0)):
                my_list.append(str((i + 1)))
        return my_list
            

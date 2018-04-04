"""
First Posotion of Target
"""

class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        length = len(nums)
        middle = length / 2
        start = 0
        end = length - 1
        while(middle > 0 and middle <(length-1)):
            if(nums[middle] == target and (nums[middle] > nums[middle - 1])):
                return middle
            if(middle == start or middle == end):
                break
            
            else:
                if(nums[middle] < target):
                    start = middle
                    middle = start + (end - middle) / 2
                     
                else:
                    end = middle
                    middle = start + (middle - start) / 2
        if(nums[middle] != target):
            return -1
        else:
            return middle
                

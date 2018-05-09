#Reverse Rotated Sorted List
#难点在于函数不返回值，list[0:n]并不能对指定内存位置的列表进行修改。故需注意引用的问题。
class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        stregth = len(nums)
        flag = None
        for i in range(len(nums)):
            if(i == len(nums) - 1):
                break
            if(nums[i] > nums[i+1]):
                flag = i
                break
        if(flag != None):
            for _ in range(flag+1):
                nums.append(nums[0])
                del nums[0]

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        up = [0]*len(nums)
        down = [0]*len(nums)
        up[0] = 1
        down[0] = 1
        
        for i in range(1,len(nums)):
            if(nums[i] > nums[i-1]):
                up[i] = down[i-1] + 1
                down[i] = down[i-1]
            if(nums[i] < nums[i-1]):
                up[i] = up[i-1]
                down[i] = up[i-1] + 1
            if(nums[i] == nums[i-1]):
                up[i] = up[i-1]
                down[i] = down[i-1]
                
        return max(up[-1],down[-1])

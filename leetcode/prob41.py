class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 1
        
        
        hashList = [0 for i in range(len(nums))]
        res = 0
        maxData = 0
            
        for i in range(len(nums)):
            if(nums[i] > 0 and nums[i] <= len(nums)):
                hashList[nums[i]-1] = nums[i]
        
        pointer = 0    
        for i in range(len(hashList)):
            pointer += 1
            if(hashList[i] == 0):
                res = i + 1
                break
        if(res == 0):
            res = pointer + 1
            
                
        return res

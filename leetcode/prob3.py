"""
Solution1:Sliding Window
#此种方法无法通过最后一个测试用例，实际上算法复杂度仍然很高，为On*2

class Solution(object):
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(s == ""):
            return 0
        if(len(s) == 1):
            return 1
        MaxList = []
        for i in range(len(s)):
            WindowBegin = i
            WindowEnd = i + 1
            HashList = []
            for _ in range(128):
                HashList.append(0)
            while(WindowEnd<=len(s)):
                if(HashList[ord(s[WindowEnd-1]) - ord('a')] == 0):
                    HashList[ord(s[WindowEnd-1]) - ord('a')] = 1
                    if(WindowEnd == len(s)):
                        MaxList.append(WindowEnd - WindowBegin)
                    else:
                        WindowEnd += 1
                else:
                    MaxList.append(WindowEnd - WindowBegin - 1)
                    break
            
            
        return max(MaxList)
"""

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

        
"""
Solution2:Sliding Window with Optimization
上一种算法使用的是穷举的方式，获得所有的可能子序列并进行重复性测试。但是算法复杂度太高。
本算法仍然使用滑动窗口的形式，但是通过添加类似动态规划的思想，减少大量的重复性计算。
def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        CharMap = {}
        start = 0
        MaxLength = 0
        for i in range(len(s)):
            if(s[i] in CharMap and start <= CharMap[s[i]]):
                start = CharMap[s[i]] + 1
            else:
                MaxLength = max(MaxLength,(i - start + 1))
                
            CharMap[s[i]] = i
            
        return MaxLength

"""

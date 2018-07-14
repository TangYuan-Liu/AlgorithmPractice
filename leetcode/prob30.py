"""
与所有单词相关联的字串
"""

"""
第一次写的结果，最后一个测试用例过不了，超时。
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
        if not words:
            return []
        if not s:
            return []
        
        singleLength = len(words[0])
        length = len(words[0]) * len(words)
        count = len(words)
        res = []
        sta = [1 for i in range(count)]
        
        for i in range(len(s)):
            if(i+length > len(s) + 1):
                break
            else:
                ha = [0 for k in range(count)]
                #ha = 0
                temp = s[i:i+length]
                j = 0
                flag = 0
                while(j <= count-1):
                    com = temp[0+j*singleLength:0+(j+1)*singleLength]
                    flag = 0
                    for m in range(count):
                        if(words[m] == com and ha[m] == 0):
                            ha[m] = 1
                            flag = 1
                            break
                    j += 1
                    if(flag == 0):
                        break
                
                if(ha == sta):
                    res.append(i)
        
        return res
"""

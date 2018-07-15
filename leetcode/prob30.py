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
        
"""
后来经过看他人算法后，发现需要维护一个dict来记录某个word出现的次数，如果次数超过，则直接break即可。算法正好可以将最后一个测试用例通过。
"""
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
        
        wordsMap = {}
        for word in words:
            if(word not in wordsMap):
                wordsMap[word] = 1
            else:
                wordsMap[word] += 1
                
        wordLen = len(words[0])
        wordSize = len(words)
        ans = []
        
        for i in range(len(s) - wordLen*wordSize+1):
            j = 0
            currDict = {}
            while(j < wordSize):
                word = s[i+j*wordLen: i+(j+1)*wordLen]
                if word not in wordsMap:
                    break
                if word not in currDict:
                    currDict[word] = 1
                else:
                    currDict[word] += 1
                if currDict[word] > wordsMap[word]:
                    break
                j += 1
            if(j == wordSize):
                ans.append(i)
                
        return ans

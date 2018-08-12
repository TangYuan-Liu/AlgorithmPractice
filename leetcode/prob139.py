class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        if not s:
            return True
        
        if not wordDict:
            return False
        
        cache = [False for _ in range(len(s) + 1)]
        cache[0] = True
        max_length = self.findMax(wordDict)
        
        for i in range(1,len(s)+1):
            j = 1
            while(j<=max_length and j<=i):
                if not cache[i-j]:
                    j += 1
                    continue
                else:
                    if s[i-j:i] in wordDict:
                        cache[i] = True
                        break                 
                j += 1            
        return cache[len(s)]
              
    def findMax(self,wordlist):
        temp = 0
        for item in wordlist:
            temp = max(temp,len(item))
            
        return temp

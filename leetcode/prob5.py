#最长回文子串

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if(len(s) == 0):
            return None
        if(len(s) == 1):
            return s
        
        start = 0
        end = start + 2
        sublist = []
        currentlongest = None
        for i in range(len(s)):
            if(end == len(s)):
                break
            else:
                if(s[start] == s[end]):
                    sublist.append([start,end])
                start += 1
                end += 1
        start = 0
        end = start + 1
        for i in range(len(s)):
            if(end == len(s)):
                break
            else:
                if(s[start] == s[end]):
                    sublist.append([start,end])
                start += 1
                end += 1
        
        if(len(sublist) == 0):
            return s[0]
        currentlongest = s[sublist[0][0]:sublist[0][1]+1]
        
        for i in range(len(sublist)):
            start = sublist[i][0]
            end = sublist[i][1]
            while(start-1>=0 and end+1<=len(s)-1):
                if(s[start-1] != s[end+1]):
                    break
                else:
                    if(end-start+3 > len(currentlongest)):
                        currentlongest = s[start-1:end+2]
                    start -= 1
                    end += 1
        
        return currentlongest

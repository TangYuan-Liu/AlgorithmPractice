class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0
        
        stack = []
        res = 0
        start = 0
        for i in range(len(s)):
            if(s[i] == '('):
                stack.append(i)
            else:
                if(len(stack) == 0):
                    start = i + 1
                else:
                    stack.pop()
                    if(len(stack) == 0):
                        res = max(res, i-start+1)
                    else:
                        res = max(res, i - stack[-1])
                        
        return res

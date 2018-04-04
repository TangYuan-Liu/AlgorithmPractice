"""
Merge Two Sorted Array
"""

class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        length = len(A) + len(B)
        A = A + B
        for i in range (length - 1):
            min_num = i + 1
            for j in range(i+1,length):
                if(A[j] < A[min_num]):
                    min_num = j
            if(A[min_num] < A[i]):
                help = A[i]
                A[i] = A[min_num]
                A[min_num] = help
        
        return A
            
                
                
        
        

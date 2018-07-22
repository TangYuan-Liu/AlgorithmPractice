class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solve()
        
        
    def findBlank(self):
        for i in range(9):
            for j in range(9):
                if(self.board[i][j] == '.'):
                    return i,j
                
        return -1, -1
    
    def isSafe(self, row, col, num):
        subrowStart = row - (row % 3)
        subcolStart = col - (col % 3)
        if(self.checkrow(row, num) and self.checkcol(col, num) and self.checkBox(subrowStart, subcolStart, num)):
            return True
        
        return False
    
    def checkrow(self,row, num):
        for col in range(9):
            if(self.board[row][col] == num):
                return False
            
        return True
            
    def checkcol(self, col, num):
        for row in range(9):
            if(self.board[row][col] == num):
                return False
            
        return True
    
    def checkBox(self, row, col, num):
        for r in range(row, row+3):
            for c in range(col, col+3):
                if(self.board[r][c] == num):
                    return False
                
        return True
                            
    def solve(self):
        row, col = self.findBlank()
        if(row == -1 and col == -1):
            return True
        for num in ['1','2','3','4','5','6','7','8','9']:
            if self.isSafe(row, col, num):
                self.board[row][col] = num
                if(self.solve()):
                    return True
                    
                self.board[row][col] = '.'
        return False

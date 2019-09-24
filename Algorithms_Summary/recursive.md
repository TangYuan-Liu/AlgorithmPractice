# Algorithms Summary--Recursive

## 递归两要素
* 递归条件
* 退出条件

## 示例1（leetcode 529 扫雷游戏）
<pre><code>
class Solution(object):  
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        x = click[0]
        y = click[1]
        lenx = len(board)
        leny = len(board[0])
        
        if not board or not click:
            return board
        
        x, y = click[0], click[1]
        lenx, leny = len(board),len(board[0])
        
        if(board[x][y] == 'M'):
            board[x][y] = 'X'
            return board
        
        dx = [1,1,1,0,0,-1,-1,-1]
        dy = [1,0,-1,1,-1,1,0,-1]
        record = [[0]*leny for _ in range(lenx)]
        
        def dfs(_x,_y):
            if(board[_x][_y] == 'M' or record[_x][_y] == 1):
                return
            record[_x][_y] = 1
            cnt = 0
            for i in range(8):
                cx = _x + dx[i]
                cy = _y + dy[i]
                
                if( 0 <= cx < lenx and 0 <= cy < leny):
                    if(board[cx][cy] == 'M'):
                        cnt += 1
            if(cnt > 0):
                board[_x][_y] = str(cnt)
                return 
            else:
                board[_x][_y] = 'B'
                
                for i in range(8):
                    cx = _x + dx[i]
                    cy = _y + dy[i]
                    
                    if( 0 <= cx < lenx and 0 <= cy < leny):
                        dfs(cx, cy)
    
        dfs(x,y)
        return board        
</code></pre>

## 应用场景1：深度与广度搜索
在树的遍历过程中，决定深度还是广度搜索的重要特点为递归分支的顺序。而在具体的实现中，树的广度搜索使用**队列**与**while循环**，完成实际的高效实现。

## 与编程语言的结合
### Python
传入的对象无需复制，直接使用return返回，无需添加返回值。
### C/C++
函数传入大概率为指针，同样不需要复制对象。
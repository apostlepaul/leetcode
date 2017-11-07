class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        def crush(b):
            row = len(board)
            col = len(board[0])
            flag = False
            for i in range(row):
                for j in range(col-2):
                    if b[i][j] != 0 and abs(b[i][j]) == abs(b[i][j+1]) == abs(b[i][j+2]):
                        flag = True
                        b[i][j] = b[i][j+1] =b[i][j+2] = -abs(b[i][j])
            for j in range(col):
                for i in range(row-2):
                    if b[i][j] != 0 and abs(b[i][j]) == abs(b[i+1][j]) == abs(b[i+2][j]):
                        flag = True
                        b[i][j] = b[i+1][j] =b[i+2][j] = -abs(b[i][j])
            for i in range(row):
                for j in range(col):
                    if b[i][j] < 0:
                        b[i][j] =0
            return flag
                        
        def move_down(b):
            row = len(b)
            col = len(b[0])
            for j in range(col):
                down_zero = 0
                index_down_num = [0]*row
                for i in range(row)[::-1]:
                    if b[i][j] == 0:
                        down_zero += 1
                    else:
                        index_down_num[i] = down_zero
                for i in range(row)[::-1]:
                    if index_down_num[i] != 0:
                        b[i+index_down_num[i]][j] = b[i][j]
                for i in range(down_zero):
                    b[i][j] = 0
                                
                    
        while True:
            if crush(board):
                move_down(board)
            else:
                break
        return board

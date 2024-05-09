"""
<Description>
Given the M*N board.
We cut the board with 8*8 size and then print the square piece of the board again.
Now, we can choose 8*8 size piece of the board anywhere. 
The board must be printed black and white alternately.
Get the minimum of the sqare piece of board that we have to print again.

<Variables>
- M : a num of chessboard's row (8<=M<=50)
- N : a num of chessboard's column (8<=N<=50)
- board : the elements of chessboard (M*N)

<Algorithm>
-
"""

def check_min(chessboard):
    result = []
    for i in range(len(chessboard)-7):
        for j in range(len(chessboard[0])-7):
            cnt1, cnt2 = 0, 0
            for a in range(i, i+8):
                for b in range(j, j+8):
                    if (a+b) % 2 == 0:
                        if board[a][b] != 'W':
                            cnt1 += 1
                        elif board[a][b] != 'B':
                            cnt2 += 1
                    elif (a+b) % 2 == 1:
                        if board[a][b] != 'B':
                            cnt1 += 1
                        elif board[a][b] != 'W':
                            cnt2 += 1
            result.append(cnt1)
            result.append(cnt2)
    return min(result)

M, N = map(int, input().split())
board = []
for _ in range(M):
    board.append(input())
print(check_min(board))
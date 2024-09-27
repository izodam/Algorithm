import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]
# 첫 줄은 무조건 오른쪽으로만 이동 가능
dp[0][0] = board[0][0]
for i in range(1, m):
    dp[0][i] = dp[0][i-1] + board[0][i]

for row in range(1, n):
    left_to_right = [0] * m
    right_to_left = [0] * m

    left_to_right[0] = dp[row-1][0] + board[row][0]
    for i in range(1, m):
        left_to_right[i] = max(left_to_right[i-1], dp[row-1][i]) + board[row][i]
    
    right_to_left[-1] = dp[row-1][-1] + board[row][-1]
    for i in range(m-2, -1, -1):
        right_to_left[i] = max(right_to_left[i+1], dp[row-1][i]) + board[row][i]
    
    for i in range(m):
        dp[row][i] = max(left_to_right[i], right_to_left[i])

print(dp[-1][-1])
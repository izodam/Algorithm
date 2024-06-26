import sys
input = sys.stdin.readline

# 14890. 경사로

# 낮은 칸과 높은 칸의 높이 차이는 1이여야
# 경사로는 낮은 칸에 놓이며, L개의 연속된 칸에 모두 접해야 함 -> L개의 연속된 칸이 높이가 모두 같아야 함

def set_load(board):
    global res
    for i in range(n):
        before_height = board[i][0]
        visited = [0] * n

        idx = 1
        while idx < n:
            # 낮아진 경우
            if before_height - board[i][idx] == 1:
                if 0 <= idx + l - 1 < n and board[i][idx:idx + l] == [board[i][idx]] * l and 1 not in visited[idx:idx + l]:
                    before_height = board[i][idx]
                    visited[idx:idx + l] = [1] * l
                    idx = idx + l
                else:
                    break

            # 높아진 경우
            elif before_height - board[i][idx] == -1:
                if 0 <= idx - l < n and board[i][idx - l:idx] == [before_height] * l and 1 not in visited[idx - l:idx]:
                    before_height = board[i][idx]
                    idx = idx + 1
                else:
                    break

            # 이전과 높이가 같은 경우
            elif before_height == board[i][idx]:
                idx += 1

            else:
                break

        else:
            res += 1


n, l = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

res = 0
# 가로 확인
set_load(board)

# 세로 확인 위해 보드판 전치
board = list(map(list, zip(*board)))

set_load(board)

print(res)
# 14503 로봇 청소기
# 소요시간 - 15분 but 틀림


import sys
input = sys.stdin.readline

def move_robot(r, c, d):
    # 반시계 = index - 1
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    res = 0

    while True:
        # 청소 완료된 경우 3으로 표시
        if board[r][c] == 0:
            res += 1
            board[r][c] = 3


        for i in range(1, 5):
            d = (d - 1) % 4
            if 0 <= r + direction[d][0]< n and 0 <= c + direction[d][1] < m and board[r + direction[d][0]][c + direction[d][1]] == 0:
                r += direction[d][0]
                c += direction[d][1]
                break
        else:
            back = (d - 2) % 4
            if board[r + direction[back][0]][c + direction[back][1]] == 1:
                return res
            else:
                r += direction[back][0]
                c += direction[back][1]

# 처음에 빈 칸은 전부 청소되지 않은 상태
# 1. 청소되지 않은 경우, 현재 칸을 청소
# 2. 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우 - 후진하고 1번으로 돌아감 / 후진 못하면 작동 멈춤
# 3. 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우 - 반시계로 90도 회전 후 청소되지 않은 칸이면 전진
n, m = map(int,input().split())
# 로봇 청소기 초기 위치 (r,c)와 방향 d
# d = 0: 북, 1: 동, 2: 남, 3: 서
r, c, d = map(int,input().split())
# 0은 청소되지 않은 칸, 1은 벽
board = [list(map(int,input().split())) for _ in range(n)]

print(move_robot(r ,c, d))
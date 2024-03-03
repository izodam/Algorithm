delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

direction = [{0: 2, 1: 0, 2: 3, 3: 1},
             {0: 1, 1: 2, 2: 3, 3: 0},
             {0: 1, 1: 3, 2: 0, 3: 2},
             {0: 3, 1: 0, 2: 1, 3: 2},
             {0: 1, 1: 0, 2: 3, 3: 2}]

# k = delta index
def move(x, y, k):
    score = 0
    nx, ny = x + delta[k][0], y + delta[k][1]
    while True:
        # 종료 조건
        if nx == x and ny == y:
            return score

        elif board[nx][ny] == -1:
            return score

        # 블록 부딪히면 점수 추가
        elif 1 <= board[nx][ny] <= 5:
            score += 1
            k = direction[board[nx][ny] - 1][k]

        # 웜홀 빠지면 위치 변경
        elif board[nx][ny] >= 6:
            idx_list = hole[board[nx][ny]]
            for i, j in idx_list:
                if i != nx or j != ny:
                    nx, ny = i, j
                    break

        nx += delta[k][0]
        ny += delta[k][1]


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    # -1 = 블랙홀, 1~5 = 블록, 6~10 = 웜홀
    board = [[5]*(n+2)] + [[5]+list(map(int, input().split()))+[5] for _ in range(n)] + [[5]*(n+2)]
    # 웜홀과 블랙홀 위치 받아놓기
    hole = {}
    for i in range(1, n+1):
        for j in range(1, n+1):
            if board[i][j] >= 6:
                if board[i][j] in hole:
                    hole[board[i][j]].append((i, j))
                else:
                    hole[board[i][j]] = [(i, j)]

    # print(black, hole)
    res = 0
    # i, j = 시작 위치
    # k = 이동 방향
    for i in range(1, n+1):
        for j in range(1, n+1):
            if board[i][j] == 0:
                for k in range(4):
                    score = move(i, j, k)
                    res = max(res, score)
    print(f'#{tc}', res)
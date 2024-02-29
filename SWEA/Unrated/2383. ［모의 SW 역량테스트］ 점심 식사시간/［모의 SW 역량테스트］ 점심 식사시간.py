from itertools import combinations

def move(people, stair):
    t = []
    for person in people:
        t.append(abs(person[1] - stair[1]) + abs(person[0] - stair[0]))
    t.sort()
    # print(t)

    # 이 계단으로 내려가는 사람 수
    l = len(people)
    # 내려가는데 걸리는 시간
    down = board[stair[0]][stair[1]] + 1

    if l == 0:
        return 0

    if l > 3:
        for i in range(l - 3):
            if t[i] + down <= t[i+3]:
                continue
            t[i+3] = t[i] + down - 1
    time = t[-1] + down

    return time



T = int(input())
for tc in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    people = []
    stair = []

    res = float('inf')


    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                people.append((i, j))
            elif board[i][j] >= 2:
                stair.append((i,j))


    for i in range(n):
        for people1 in combinations(people, i):
            people2 = list(set(people) - set(people1))
            now = max(move(people1, stair[0]), move(people2, stair[1]))
            res = min(res, now)
    print(f'#{tc}', res)
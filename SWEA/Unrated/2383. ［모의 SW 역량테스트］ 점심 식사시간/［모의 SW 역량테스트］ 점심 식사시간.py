from itertools import combinations
from collections import deque


def move(people, stair):
    # 계단까지의 시간
    t = []

    for person in people:
        t.append(abs(person[0] - stair[0]) + abs(person[1] - stair[1]))

    t = deque(sorted(t))

    # 내려가는데 걸리는 시간
    down = graph[stair[0]][stair[1]]

    # 계단 안 상황
    in_stair = deque()

    time = 0
    stair_people = 0

    while t:
        time += 1

        # 해당 시간에 도착한 애 있으면 빼주기
        while in_stair and in_stair[0] == time:
            in_stair.popleft()
            stair_people -= 1

        # 해당 시간에 계단 도착하면
        while t[0] < time:
            if stair_people < 3:
                t.popleft()
                # 남은 사람 없으면 마지막 사람 내려보내고 끝내기
                if not t:
                    time += down
                    break

                # 그게 아니라면 계단 안에 넣어줌
                in_stair.append(time+down)
                stair_people += 1
            # 계단 꽉차있으면 이번 시간은 pass
            else:
                break

    return time


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    # 1 = 사람, 2 이상 = 계단 입구 (계단 길이)
    # 계단 입구 무조건 2개
    # 계단 위에는 동시에 최대 3명까지만 올라가 있을 수 있다
    # 계단 입구에 도착하면, 1분 후 아래칸으로 내려 갈 수 있다 -> 도착 후 계단길이 + 1 소요
    graph = [list(map(int,input().split())) for _ in range(n)]

    people = []
    stair = []
    res = float('inf')

    # 사람, 계단 위치 저장
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                people.append((i, j))
            elif graph[i][j] >= 2:
                stair.append((i, j))

    # 1번 계단에 i명 이동 시킴
    for i in range(n):
        for people1 in combinations(people, i):
            people2 = list(set(people) - set(people1))
            time = max(move(people1, stair[0]), move(people2, stair[1]))
            res = min(res, time)


    print(f'#{tc}',res)
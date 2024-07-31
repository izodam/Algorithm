import sys
input = sys.stdin.readline
import heapq

z = int(input())
for tc in range(z):
    # n은 호수의 개수, m은 호수에 비가 내리는 날
    n, m = map(int,input().split())
    # 0이라면 i번째 날에는 비가 오지 않음 -> 용이 물 마심
    rainy_day = list((map(int,input().split())))
    # 호수 채워져있는지 확인 ->  채워져있으면 1
    lake = [1] * (n + 1)
    # 해당 호수에 비가 왔었는지 확인용
    past = [-1] * (n + 1)
    # i번째 날짜 다음에 확인해야 하는 날(비가 오는 같은 호수 중 i번째 날짜 다음 가장 빠른 날)
    next_day = [-1] * m

    res = []

    # 우선순위 큐
    # 먼저 마셔야 할 날짜
    hq =[]

    for i in range(m):
        # i번째 날에 비가 온다면
        if rainy_day[i]:
            # 해당 호수가 이전에 비가 온적이 없다면 날짜 우선순위 큐에 넣어주기
            if past[rainy_day[i]] == -1:
                heapq.heappush(hq, i)
            # 비온적이 있다면 대기
            else:
                next_day[past[rainy_day[i]]] = i
            past[rainy_day[i]] = i

    for i in range(m):
        # 비가 온다면
        if rainy_day[i]:
            # 물이 차 있다면
            if lake[rainy_day[i]]:
                print("NO")
                break
            else:
                lake[rainy_day[i]] = 1
                # 마셔야 할 호수에 다음 날짜 추가
                if next_day[i] != -1:
                    heapq.heappush(hq, next_day[i])
        else:
            if hq:
                drink = heapq.heappop(hq)
                res.append(rainy_day[drink])
                lake[rainy_day[drink]] = 0
            else:
                res.append(0)
    else:
        print("YES")
        print(' '.join(map(str, res)))
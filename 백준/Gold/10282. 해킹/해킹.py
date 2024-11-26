import sys
input = sys.stdin.readline

import heapq

t = int(input())
for tc in range(t):
    # 컴퓨터 개수 n, 의존성 개수 d, 해킹당한 컴퓨터의 번호 c
    n, d, c = map(int, input().split())
    # a가 컴퓨터 b를 의존하며, 컴퓨터 b가 감염되면 s초 후 컴퓨터 a도 감염
    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    q = []
    visited = [float('inf')] * (n+1)

    visited[c] = 0
    heapq.heappush(q, (c, 0))


    while q:
        computer, time = heapq.heappop(q)
        for next_computer in graph[computer]:
            if visited[next_computer[0]] > time + next_computer[1]:
                heapq.heappush(q, (next_computer[0], time + next_computer[1]))
                visited[next_computer[0]] = time + next_computer[1]

    cnt = 0
    last_time = 0
    for time in visited:
        if time != float('inf'):
            cnt += 1
            last_time = max(last_time, time)
    print(cnt, last_time)
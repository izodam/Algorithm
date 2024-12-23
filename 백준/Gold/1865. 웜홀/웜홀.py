# 웜홀은 음수 가중치
# 음수 사이클이 있는지만 확인하면 된다
import sys
input = sys.stdin.readline

TC = int(input())
INF = int(1e9)

def bellmanFord():
    for i in range(n):
        for s, e, t in graph:
            cost = dist[s] + t
            if cost < dist[e]:
                dist[e] = cost
                if i == n-1:
                    return False
    return True

for tc in range(TC):
    # 지점의 수 n, 도로의 개수 m, 웜홀의 개수 w
    n, m, w = map(int,input().split())
    graph = []

    for _ in range(m):
        # S와 E는 연결된 지점의 번호(방향이 없음), T는 이 도로를 통해 이동하는데 걸리는 시간
        s, e, t = map(int,input().split())
        graph.append((s, e, t))
        graph.append((e, s, t))
    for _ in range(w):
        # S는 시작 지점, E는 도착 지점(방향이 있음), T는 줄어드는 시간
        s, e, t = map(int,input().split())
        graph.append((s, e, -t))

    dist = [INF] * (n + 1)
    if bellmanFord():
        print("NO")
    else:
        print("YES")
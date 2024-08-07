# 16118. 달빛 여우 - 다익스트라??

# N개의 나무 그루터기, M개의 오솔길
# 달빛 여우와 달빛 늑대는 1번 나무 그루터기
# 달빛 여우는 늘 일정한 속도
# 달빛 늑대는 달빛 여우보다 더 빠르게 달릴 수 있지만 체력이 부족하기 때문에 다른 전략
# 출발할 때 오솔길 하나를 달빛 여우의 두 배의 속도로 달려가고,
# 그 뒤로는 오솔길 하나를 달빛 여우의 절반의 속도로 걸어가며 체력을 회복하는 것을 반복
# 달빛 여우가 달빛 늑대보다 먼저 도착할 수 있는 그루터기에 개수

import heapq
import sys
input = sys.stdin.readline

def dij_fox():
    q = []
    # distance, node
    heapq.heappush(q, (0, 1))

    while q:
        current_distance, current_node = heapq.heappop(q)

        if distance_fox[current_node] < current_distance:
            continue

        for new_node, new_distance in graph[current_node]:
            dis = new_distance + current_distance

            if dis < distance_fox[new_node]:
                distance_fox[new_node] = dis
                heapq.heappush(q, (dis, new_node))

def dij_wolf():
    q = []
    # distance, node, 2배속인지 여부
    heapq.heappush(q, (0, 1, 0))

    while q:
        current_distance, current_node, is_run = heapq.heappop(q)

        if is_run and distance_wolf[0][current_node] < current_distance:
            continue
        
        elif not is_run and distance_wolf[1][current_node] < current_distance:
            continue
        
        for new_node, new_distance in graph[current_node]:
            # 2배속으로 도착한 노드라면, 이제는 0.5배속 -> 거리 2배 됨
            if is_run:
                dis = (new_distance * 2) + current_distance

                if dis < distance_wolf[1][new_node]:
                    distance_wolf[1][new_node] = dis
                    heapq.heappush(q, (dis, new_node, 0))
            else:
                dis = (new_distance // 2) + current_distance

                if dis < distance_wolf[0][new_node]:
                    distance_wolf[0][new_node] = dis
                    heapq.heappush(q, (dis, new_node, 1))




n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]


for _ in range(m):
    n1, n2, dis = map(int,input().split())
    graph[n1].append((n2, dis*2))
    graph[n2].append((n1, dis*2))

distance_fox = [float('inf')] * (n + 1)
# 절반 속도, 두 배 속도
distance_wolf = [[float('inf')] * (n+1) for _ in range(2)]


# 시작점의 distance는 0
distance_fox[1] = 0
distance_wolf[1][1] = 0

dij_fox()
dij_wolf()

res = 0

for i in range(1, n+1):
    if distance_fox[i] < min(distance_wolf[0][i], distance_wolf[1][i]):
        res += 1
print(res)
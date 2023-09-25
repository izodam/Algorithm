import sys
input = sys.stdin.readline

n,m,b = map(int,input().split())
graph = {}  # 높이 저장. key=높이, value=해당 높이 개수

for _ in range(n):
    i = list(map(int,input().split()))
    for j in i:
        if j in graph:
            graph[j] += 1
        else:
            graph[j] = 1

high = max(graph.keys())
low = min(graph.keys())

t = 1000000000
height = 0
for i in range(low,high+1):
    inventory = 0
    plant = 0
    for key,value in graph.items():
        if key > i:
            inventory += (key-i)*value
        else:
            plant += (i-key)*value
    if inventory+b < plant:
        continue
    else:
        now_time = (inventory*2)+plant
        if t >= now_time:
            t = now_time
            height = i

print(t,height)
import sys
input = sys.stdin.readline

def bisearch(num):
    if visited[num]:
        return False
    visited[num] = 1


    for number in graph[num]:
        if select[number] == -1 or bisearch(select[number]):
            select[number] = num
            return True
    return False

n, m = map(int,input().split())

graph = []
for _ in range(n):
    cnt, *arr = map(int,input().split())
    graph.append(arr)

select = [-1] * (m + 1)

for work in range(2):
    for person in range(n):
        visited = [0] * n
        bisearch(person)

print(sum([1 for i in select if i > -1]))
import sys
input = sys.stdin.readline
from  collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    global res
    doors = []
    q = deque()
    q.append((x, y))
    graph[x][y] = '0'
    while q:
        x, y = q.popleft()
        # print(doors)
        # print(keys)
        # print('\n'.join(map(str, graph)))
        # print('--------------------------------------------------------------------')
        for i in range(4):
            nx, ny = x + dx[i], y+dy[i]
            if 0 <= nx <= h+1 and 0 <= ny <= w+1:
                if graph[nx][ny] == '0' or graph[nx][ny] == '*':
                    continue
                # 빈공간일때
                if graph[nx][ny] == '.':
                    q.append((nx, ny))
                    graph[nx][ny] = '0'

                # 문서일 때
                elif graph[nx][ny] == '$':
                    res += 1
                    q.append((nx, ny))
                    graph[nx][ny] = '0'
                    # print(res)
                    # print('doors:', doors)
                    # print('keys: ',keys)
                    # print('q', q)
                    # print('\n'.join(map(str, graph)))
                    # print('----------------------------------------------------------------------')

                # 문일때
                elif graph[nx][ny].isupper():
                    if graph[nx][ny] in keys:
                        q.append((nx, ny))
                    else:
                        doors.append((nx, ny, graph[nx][ny]))
                    graph[nx][ny] = '0'


                # 키일때
                elif graph[nx][ny].islower():
                    key = graph[nx][ny].upper()
                    keys.add(key)
                    new_door = doors.copy()
                    for r, c, door in new_door:
                        # print(f'here is door! {key}, {r},{c},{door}')
                        if key == door:
                            q.append((r, c))
                            doors.remove((r, c, door))
                    # print(doors)
                    # print(keys)
                    # print('----------------------------------------------------------------------')

                    q.append((nx, ny))
                    graph[nx][ny] = '0'


tc = int(input())

for _ in range(tc):
    h, w = map(int, input().split())
    # . : 빈공간, * : 벽, $ : 문서, 대문자: 문, 소문자: 열쇠 (해당하는 문자의 대문자 문에 해당)
    graph = [['.']+list(input().strip())+['.'] for _ in range(h)]
    # side =
    graph = [['.'] * (w+2)] + graph + [['.'] * (w+2)]

    keys = set()
    k = input().strip()
    if k.isalpha():
        for i in k:
            keys.add(i.upper())
    # print(keys)
    # print('\n'.join(map(str,graph)))

    res = 0
    bfs(0,0)


    print(res)
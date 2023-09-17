from collections import deque
import sys
input = sys.stdin.readline

def bfs(a,b):
    q = deque()
    q.append((a,''))
    visited = [False]*10000
    visited[a] = True

    while q:
        n,res= q.popleft()

        if n==b:
            return res
        #D
        num = (n*2)%10000
        if not visited[num]:
            q.append((num,res+'D'))
            visited[num] = True

        #S
        num = (n-1)%10000
        if not visited[num]:
            q.append((num,res+'S'))
            visited[num] = True

        #L
        num = (10*n+(n//1000))%10000
        if not visited[num]:
            q.append((num,res+'L'))
            visited[num] = True

        #R
        num = (n//10+(n%10)*1000)%10000
        if not visited[num]:
            q.append((num, res + 'R'))
            visited[num] = True


T = int(input())
for i in range(T):
    A,B = map(int,input().split())  # A:레지스터 초기값, B:최종 값
    print(bfs(A,B))

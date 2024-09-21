import sys
input = sys.stdin.readline

def find():
    cnt = 0
    for c in choice:
        for i in range(c[0], c[1] + 1):
            if not visited[i]:
                visited[i] = 1
                cnt += 1
                break
    return cnt

t = int(input())

for tc in range(t):
    n, m = map(int,input().split())
    choice = [list(map(int,input().split())) for _ in range(m)]
    choice.sort(key=lambda x: (x[1], x[0]))

    visited = [0]*(n+1)
    print(find())
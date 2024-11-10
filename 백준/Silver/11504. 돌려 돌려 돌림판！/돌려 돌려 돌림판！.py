import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x = int(''.join(input().split()))
    y = int(''.join(input().split()))
    circle = list(input().split())
    new = circle + circle[:m-1]
    cnt = 0
    tmp = 0
    for i in range(n):
        tmp = int(''.join(new[i:i+m]))
        if x <= tmp <= y:
            cnt += 1
    print(cnt)
import sys
input = sys.stdin.readline

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    cnt = 0
    start = 0
    for i in a:
        while True:
            if start == m or i <= b[start]:
                cnt += start
                break
            start += 1
    print(cnt)
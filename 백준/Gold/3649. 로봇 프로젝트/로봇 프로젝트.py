import sys
input = sys.stdin.readline

while True:
    x_input = input()
    if x_input == "":
        break

    x = int(x_input)
    x *= 10**7
    n = int(input())
    l = [int(input()) for _ in range(n)]
    l.sort()

    start = 0
    end = n-1

    res = []

    while start < end:
        now = l[start] + l[end]
        if now == x:
            res.append((l[start], l[end]))
            start += 1
        elif now > x:
            end -= 1
        else:
            start += 1

    if res:
        res.sort(key=lambda x: abs(x[1]-x[0]))
        print('yes', res[-1][0], res[-1][1])
    else:
        print('danger')
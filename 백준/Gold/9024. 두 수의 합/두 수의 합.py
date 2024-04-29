import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n, k = map(int,input().split())
    nums = sorted(list(map(int,input().split())))

    close = float('inf')
    res = 0

    start, end = 0, n-1

    while start < end:
        now = nums[start] + nums[end]
        if abs(k-now) < close:
            close = abs(k-now)
            res = 1

        elif abs(k-now) == close:
            res += 1

        if k - now > 0:
            start += 1
        else:
            end -= 1

    print(res)
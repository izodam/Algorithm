import sys
input = sys.stdin.readline
n = int(input())
liquid = sorted(list(map(int, input().split())))

res = []
min_value = float('inf')

for i in range(n-2):
    left = i+1
    right = n-1

    while left < right:
        now = liquid[i] + liquid[left] + liquid[right]
        if abs(now) < abs(min_value):
            min_value = now
            res = [liquid[i], liquid[left], liquid[right]]

        if now < 0:
            left += 1
        elif now > 0:
            right -= 1
        else:
            # 0이면 탐색 종료
            print(*res)
            exit(0)

print(*res)
import sys
input = sys.stdin.readline

n = int(input())
h = sorted(list(map(int,input().split())))

res = float('inf')

# 먼저 2개 선택
# 사이에 적어도 2개 있어야하므로 범위는 n-3까지
for i in range(n-3):
    for j in range(i+3, n):
        one = h[i] + h[j]

        l = i + 1
        r = j - 1
        while l < r:
            another = h[l] + h[r]
            now = abs(one - another)
            res = min(res, now)
            if now == 0:
                print(0)
                exit(0)

            if one < another:
                r -= 1
            else:
                l += 1

print(res)
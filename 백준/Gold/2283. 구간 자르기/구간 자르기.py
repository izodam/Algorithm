import sys
input = sys.stdin.readline

n, k = map(int, input().split())
# 각 지점에 대한 선분 개수
line_cnt = [0] * 1000001
last = 0

for _ in range(n):
    left, right = map(int, input().split())
    last = max(last, right)
    line_cnt[left] += 1
    line_cnt[right] -= 1


# 누적합
for i in range(1, last+1):
    line_cnt[i] += line_cnt[i-1]

start, end = 0, 0
now = 0

while end <= last:
    if now == k:
        print(start, end)
        break
    elif now < k:
        now += line_cnt[end]
        end += 1
    else:
        now -= line_cnt[start]
        start += 1
else:
    print(0, 0)
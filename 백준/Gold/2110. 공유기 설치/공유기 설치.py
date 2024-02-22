# 2110
n, c = map(int,input().split())
house = [int(input()) for _ in range(n)]
house.sort()

start = 1
end = house[-1] - house[0]

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    now = house[0]
    for i in house[1:]:
        if i >= now + mid:
            cnt += 1
            now = i
    if cnt >= c:
        start = mid + 1
    else:
        end = mid - 1
print(end)
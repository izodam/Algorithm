def isValid(mid):
    low = score[0]
    high = score[0]
    d = 1

    for i in score:
        if high < i:
            high = i
        if low > i:
            low = i

        if high - low > mid:
            d += 1
            low = i
            high = i

    return m >= d



n, m = map(int, input().split())
score = list(map(int, input().split()))

start = 0
end = max(score)

res = end

while start <= end:
    mid = (start + end) // 2
    
    if isValid(mid):
        end = mid - 1
        res = min(res, mid)
    else:
        start = mid + 1

print(res)
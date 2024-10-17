def shoulder_strap(mid, k):
    count = 0
    people = len(tall)

    for i in range(people):
        if i == 0:
            if abs(tall[i] - tall[i + 1]) > mid:
                count += 1
        elif i == n - 1:
            if abs(tall[i] - tall[i - 1]) > mid:
                count += 1
        else:
            if abs(tall[i] - tall[i + 1]) > mid:
                count += 1
            elif abs(tall[i] - tall[i - 1]) > mid:
                count += 1

        if count > k:
            return False

    return True

n, k = map(int,input().split())
tall = list(map(int,input().split()))

if n == 1:
    print(0)
    exit()

max_value = max(tall)
start = 0
end = max_value
res = 0

while start <= end:
    mid = (start + end) // 2

    if shoulder_strap(mid, k):
        res = mid
        end = mid - 1
    else:
        start = mid + 1

print(res)
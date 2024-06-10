n, k = map(int,input().split())
arr = list(map(int,input().split()))

res = float('inf')

left = 0
right = 0

# 라이언 인형 개수
lion = 0

if arr[left] == 1:
    lion += 1

while left < n and right < n:
    if lion < k:
        right += 1
        if right < n and arr[right] == 1:
            lion += 1
    else:
        if lion == k:
            res = min(res, right - left + 1)
        if left < n and arr[left] == 1:
            lion -= 1
        left += 1

if res == float('inf'):
    print(-1)
else:
    print(res)
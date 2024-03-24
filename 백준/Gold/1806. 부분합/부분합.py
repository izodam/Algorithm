n, s = map(int,input().split())
arr = list(map(int,input().split()))

left, right = 0, 0
cnt = 0
res = float('inf')

while True:
    if cnt >= s:
        res = min(res, right-left)
        cnt -= arr[left]
        left += 1
    elif right == n:
        break
    else:
        cnt += arr[right]
        right += 1
if res != float('inf'):
    print(res)
else:
    print(0)
g = int(input())
now_weight = [i for i in range(1, 100001)]
remember = [i for i in range(1, 100001)]

left = 0
right = 0

res = []

while left < 100000 and right < 100000:
    tmp = now_weight[left] ** 2 - remember[right] ** 2
    if tmp == g:
        res.append(now_weight[left])
        right += 1
    elif tmp < g:
        left += 1
    else:
        right += 1

if not res:
    print(-1)
else:
    print('\n'.join(map(str, res)))
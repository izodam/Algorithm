n = int(input())
first = input().strip()
res = 0


for _ in range(n-1):
    word = input().strip()
    now = list(first)
    cnt = 0
    for i in word:
        if i in now:
            now.remove(i)
        else:
            cnt += 1
    if cnt <= 1 and len(now) <= 1:
        res += 1

print(res)
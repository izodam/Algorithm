n = int(input())
m = int(input())
s = input()

cnt = 0
i = 0
res = 0
while i < m-1:
    if s[i:i+3] == 'IOI':
        i += 2
        cnt += 1
        if cnt == n:
            res += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0


print(res)
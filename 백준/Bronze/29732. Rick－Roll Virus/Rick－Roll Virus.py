n, m, k = map(int,input().split())
s = list(input().strip())
res = ['.'] * n

for i in range(1,n+1):
    if s[i-1] == 'R':
        res[max(1, i-k)-1:min(n,i+k)] = ['R'] * (min(n, i+k)+1 - max(1, i-k))

cnt = 0
for i in res:
    if i == 'R':
        cnt += 1

if cnt > m:
    print('No')
else:
    print('Yes')
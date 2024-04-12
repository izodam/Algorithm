n, m = map(int,input().split())
ans = [input() for _ in range(n)]
checked = [input() for _ in range(n)]
for i in range(n):
    a = ans[i]
    check = checked[i]
    right = ''
    for c in a:
        right += c
        right += c
    if check != right:
        print('Not Eyfa')
        break
else:
    print('Eyfa')
n = int(input())
cnt = 1
stack = []
res = ''
for _ in range(n):
    data = int(input())
    while cnt <= data:
        stack.append(cnt)
        res += '+'
        cnt += 1
    if stack.pop() == data:
        res += '-'
    else:
        print('NO')
        exit(0)
print('\n'.join(res))


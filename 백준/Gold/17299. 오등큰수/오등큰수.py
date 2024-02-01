n = int(input())
a = list(map(int,input().split()))

count = {}

stack = [0]
res = [-1] * n

for i in a:
    if i in count.keys():
        count[i] += 1
    else:
        count[i] = 1

for i in range(1, n):
    while stack and count[a[stack[-1]]] < count[a[i]]:
        res[stack.pop()] = a[i]
    stack.append(i)

print(*res)
n = int(input())
h = [int(input()) for _ in range(n)]

stack = [0]
res = [0] * n

for i in range(1, n):
    while stack and h[stack[-1]] <= h[i]:
        index = stack.pop()
        res[index] = i - index - 1
    stack.append(i)



while stack:
    index = stack.pop()
    res[index] = n - index - 1


print(sum(res))
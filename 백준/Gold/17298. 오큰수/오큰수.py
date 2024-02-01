n = int(input())
a = list(map(int,input().split()))


# 인덱스로 접근하여 스택에 인덱스를 넣어줌
stack = [0]

# 오큰수를 찾지 못하면 -1이므로 초기화 값은 -1
res = [-1] * n

for i in range(1, n):
    while stack and a[stack[-1]] < a[i]:
        res[stack.pop()] = a[i]
    stack.append(i)

print(*res)
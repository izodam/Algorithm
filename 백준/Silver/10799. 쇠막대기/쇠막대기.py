graph = input()
stack = []

# 바로 직전 괄호 확인
# 만약 직전 괄호가 (고 지금이 )면 얘는 레이저
tmp = ''
res = 0
for i in graph:
    if i == '(':
        stack.append(i)
    # 레이저
    elif i == ')' and tmp == '(':
        stack.pop()
        res += len(stack)

    else:
        stack.pop()
        res += 1

    tmp = i
print(res)
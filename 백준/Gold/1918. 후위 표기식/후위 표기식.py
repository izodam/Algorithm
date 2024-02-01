infix = input()
stack = []
ans = []

operator = {
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2,
}

for op in infix:
    if op == '(':
        stack.append(op)

    elif op == ')':
        while True:
            pop_op = stack.pop()
            if pop_op == '(':
                break
            ans.append(pop_op)

    elif op in operator:
        if not stack:       # 스택이 비어있다면 무조건 스택에 추가
            stack.append(op)

        elif stack[-1] == '(':  # 만약 스택의 마지막 요소가 왼쪽 괄호면 무조건 위로 쌓기
            stack.append(op)

        elif operator[op] > operator[stack[-1]]: # 만약 지금 op가 스택의 마지막 요소보다 우선순위가 크다면 위로 쌓기
            stack.append(op)

        else:   # 만약 지금 op가 스택의 마지막 요소보다 우선순위가 작다면 op보다 작은애가 나올때까지 pop
            while True:
                if stack:
                    if stack[-1] == '(':  # 만약 스택의 마지막 요소가 왼쪽 괄호면 무조건 위로 쌓기
                        stack.append(op)
                        break
                    elif operator[op] > operator[stack[-1]]:
                        stack.append(op)
                        break
                    ans.append(stack.pop())
                else:
                    stack.append(op)
                    break
    else:
        ans.append(op)
while stack:
    ans.append(stack.pop())
print(''.join(ans))
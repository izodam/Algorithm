sang = input()
# 폭발 문자열
bomb = input()

stack = []
n = len(bomb)

for i in sang:
    stack.append(i)
    if ''.join(stack[-n:]) == bomb:
        for _ in range(n):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
T = int(input())
for _ in range(T):
    ps = input()
    stack = []
    try:
        for i in ps:
            if i == '(':
                stack.append(i)
            else:
                stack.pop()
        if stack:
            print("NO")
        else:
            print("YES")
    except:
        print("NO")
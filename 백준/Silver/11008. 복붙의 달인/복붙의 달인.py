t = int(input())
for tc in range(t):
    s, p = input().split()
    res = 0

    print(len(s.replace(p, ' ')))
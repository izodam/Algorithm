def back(t):
    if s == t:
        print(1)
        exit()
    if len(t) == 0:
        return 0
    if t[-1] == 'A':
         back(t[:-1])
    if t[0] == 'B':
        back(t[1:][::-1])


s = list(input())
t = list(input())
back(t)
print(0)

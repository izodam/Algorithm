t = int(input())
for _ in range(t):
    math = input().split()
    n = float(math[0])
    for i in range(1,len(math)):
        if math[i] == '@':
            n*=3
        elif math[i] == '%':
            n+=5
        else:
            n-=7
    print('%0.2f' %n)
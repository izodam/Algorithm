l = input()

if l[0] == 'c':
    res = 26
else:
    res = 10
    
for i in range(1,len(l)):
    if l[i] == 'c':
        if l[i-1] == 'c':
            res *= 25
        else:
            res *= 26
    else:
        if l[i-1] == 'd':
            res *= 9
        else:
            res *= 10
print(res)
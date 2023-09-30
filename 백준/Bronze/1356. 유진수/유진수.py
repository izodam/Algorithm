num = list(map(int,input()))
for i in range(1,len(num)):
    right = 1
    left = 1
    for j in range(0,i):
        right *= num[j]
    for j in range(i,len(num)):
        left *= num[j]
    if right==left:
        print("YES")
        break
else:
    print("NO")
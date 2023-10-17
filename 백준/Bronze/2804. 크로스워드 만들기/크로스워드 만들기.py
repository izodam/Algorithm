a,b = input().split()
index_a, index_b = -1, -1

for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            index_a = i
            index_b = j
            break
    if index_a != -1:
        break


for i in range(len(b)):
    if i == index_b:
        print(a,end='')
    else:
        for j in range(len(a)):
            if j == index_a:
                print(b[i],end='')
            else:
                print('.',end='')
    print()
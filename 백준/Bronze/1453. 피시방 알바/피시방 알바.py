n = int(input())
cus = list(map(int,input().split()))
computer = [0]*101
cnt = 0
for i in cus:
    if computer[i] == 0:
        computer[i] = 1
    else:
       cnt += 1
print(cnt)
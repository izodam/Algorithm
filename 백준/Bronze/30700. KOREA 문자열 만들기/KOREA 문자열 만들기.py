s = input()
check = ['K','O',"R", "E", "A"]
idx = 0

cnt = 0

for i in s:
    if i == check[idx % 5]:
        idx += 1
        cnt += 1


print(cnt)
num = input()
now = 0
idx = 0
while True:
    now += 1
    for i in str(now):
        if num[idx] == i:
            idx += 1
            if idx >= len(num):
                print(now)
                exit()
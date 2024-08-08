t = int(input())
for tc in range(t):
    n = int(input())
    max_number = [0, 0]
    cnt = 0
    hap = 0
    for i in range(n):
        now = int(input())
        hap += now
        if now > max_number[0]:
            cnt = 0
            max_number = [now, i+1]
        elif now == max_number[0]:
            cnt += 1
        else:
            continue

    if cnt > 0:
        print("no winner")
    elif hap - max_number[0] < max_number[0]:
        print(f'majority winner {max_number[1]}')
    else:
        print(f'minority winner {max_number[1]}')
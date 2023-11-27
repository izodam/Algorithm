while True:
    try:
        n = int(input())
    except:
        break

    num = 1     # 1로만 이루어진 수
    cnt = 1     # 자리수
    while True:
        if num % n != 0:
            num = num * 10 + 1
            cnt += 1
        else:
            break
    print(cnt)
n = int(input())
for tc in range(n):
    g = int(input())
    student_number = [int(input()) for _ in range(g)]

    if g == 1:
        print(1)
    else:
        res = 1
        while True:
            now_last = set()
            for i in student_number:
                if (i % res) in now_last:
                    res += 1
                    break
                now_last.add(i % res)
            else:
                print(res)
                break
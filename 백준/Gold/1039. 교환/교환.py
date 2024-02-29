def perm(time):
    global max_value

    if number[0] == '0':
        return

    value = int(''.join(number))
    # 중복 방지 가지치기
    if value in cheaked[time]:
        return
    # 계산된 적 없는 값이면 add
    cheaked[time].add(value)
    if time == limit:
        max_value = max(max_value, value)
        return
    else:
        for i in range(n):
            for j in range(i+1, n):
                number[i], number[j] = number[j], number[i]
                perm(time + 1)
                number[i], number[j] = number[j], number[i]





number, limit = input().split()
number = list(number)
limit = int(limit)

n = len(number)
max_value = 0
if n == 1:
    max_value = -1
else:
    # 중복 방지
    cheaked = [set() for _ in range(limit+1)]
    perm(0)
if max_value == 0:
    max_value = -1
print(max_value)
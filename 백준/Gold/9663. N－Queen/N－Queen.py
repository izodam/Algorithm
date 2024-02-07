n = int(input())

res = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        # 같은 줄에 있거나
        # 대각선 상에 있으면 False
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def n_queens(x):
    global res
    if x == n:
        res += 1
        return
    else:
        for i in range(n):
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(res)
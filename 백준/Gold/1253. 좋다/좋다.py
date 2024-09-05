import sys
input = sys.stdin.readline

def binary_search(x, idx):
    start = 0
    end = n-1

    while start < end:
        if start == idx:
            start += 1
            continue
        if end == idx:
            end -= 1
            continue
        if numbers[start] + numbers[end] == x:
            return True
        elif numbers[start] + numbers[end] > x:
            end -= 1
        else:
            start += 1
    return False

n = int(input())
numbers = sorted(list(map(int, input().split())))

res = 0
for i in range(n):
    if binary_search(numbers[i], i):
        res += 1
print(res)
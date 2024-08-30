import sys
input = sys.stdin.readline

n = int(input())
liquid = sorted(list(map(int, input().split())))

min_value = float('inf')
res = []

start = 0
end = n-1

while start < end:
    if liquid[start] + liquid[end] == 0:
        print(liquid[start], liquid[end])
        break
    elif abs(liquid[start] + liquid[end]) < min_value:
        min_value = abs(liquid[start] + liquid[end])
        res = [liquid[start], liquid[end]]
    
    if liquid[start] + liquid[end] < 0:
        start += 1
    else:
        end -= 1

print(*res)
n = int(input())
arr = sorted(list(map(int,input().split())))

target = 1
for i in arr:
  if target < i:
    break
  target += i
print(target)
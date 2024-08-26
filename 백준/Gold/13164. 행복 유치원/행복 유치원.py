n, k = map(int,input().split())
stu = list(map(int,input().split()))

arr = []

for i in range(n-1):
    arr.append(stu[i+1] - stu[i])

arr.sort()
cost = 0

for i in range(n-k):
    cost += arr[i]
print(cost)
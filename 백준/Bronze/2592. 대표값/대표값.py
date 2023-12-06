n = [int(input()) for _ in range(10)]
print(sum(n)//10)
print(max(n,key = n.count))
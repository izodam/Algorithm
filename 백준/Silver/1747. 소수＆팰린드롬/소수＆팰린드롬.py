import math

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n%i == 0:
            return False
    return True

n = int(input())

while True:
    # 펠린드롬 판별
    if str(n) == str(n)[::-1]:
        # 소수 판별
        if isPrime(n):
            print(n)
            break
    n += 1
import sys
input = sys.stdin.readline

def tickto(arr, t):
    if t == arr[0] == arr[1] == arr[2]:
        return True
    if t == arr[3] == arr[4] == arr[5]:
        return True
    if t == arr[6] == arr[7] == arr[8]:
        return True
    if t == arr[0] == arr[4] == arr[8]:
        return True
    if t == arr[2] == arr[4] == arr[6]:
        return True
    if t == arr[0] == arr[3] == arr[6]:
        return True
    if t == arr[1] == arr[4] == arr[7]:
        return True
    if t == arr[2] == arr[5] == arr[8]:
        return True
    return False

while True:
    now_input = input().strip()
    if now_input == 'end':
        break
    stone = list(map(str, now_input))
    x = stone.count('X')
    o = stone.count('O')

    if x > o+1 or o > x:
        print('invalid')
        continue

    # o가 이겨야 함
    if x == o:
        if tickto(stone, 'O') and not tickto(stone, 'X'):
            print('valid')
            continue

    # x가 이겨야 함
    if o+1 == x:
        if tickto(stone, 'X') and not tickto(stone, 'O'):
            print('valid')
            continue

    # 보드판 다 채워짐
    if x == 5 and o == 4:
        if not tickto(stone, 'O'):
            print("valid")
            continue

    print("invalid")
n = int(input())

tile = [1, 1, 2, 3, 5, 8]
if n == 1:
    print(4)
    exit()
if n > len(tile):
    for i in range(6, n):
        tile.append(tile[-1] + tile[-2])
print((tile[n-1] + tile[n-2] + tile[n-1])*2)
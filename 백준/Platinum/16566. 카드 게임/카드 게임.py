import sys
input = sys.stdin.readline

def binary_search(cards, card):
    start = 0
    end = len(cards)

    while start <= end:
        mid = (start + end) // 2
        if cards[mid] == card:
            return mid+1
        elif cards[mid] > card:
            end = mid - 1
        else: 
            start = mid + 1
    return start


n, m, k = map(int, input().split())
cards = sorted(list(map(int, input().split())))
su = list(map(int, input().split()))

visited = [0] * m

for su_card in su:
    idx = binary_search(cards, su_card)
    # print(idx)
    for i in range(idx, m):
        if not visited[i]:
            visited[i] = 1
            print(cards[i])
            break
    # print(cards)

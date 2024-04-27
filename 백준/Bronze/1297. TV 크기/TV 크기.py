d, h, w = map(int,input().split())
rate = d / (h**2 + w**2)**0.5
print(int(h*rate), int(w*rate))
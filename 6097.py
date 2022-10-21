pan = []
h, w = map(int, input().split())
for i in range(h):
    pan.append([])
    for j in range(w):
        pan[i].append(0)

n = int(input())

for i in range(n):
    l, d, x, y = map(int, input().split())
    x = x-1
    y = y-1
    for j in range(l):
        if d == 0 :
            # 가로
            pan[x][y+j] = 1
        else :
            # 세로
            pan[x+j][y] = 1

for i in range(h):
    for j in range(w):
        print(pan[i][j], end = " ")
    print()
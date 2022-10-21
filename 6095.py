h = 19
w = 19
d = []

for i in range(h):
    d.append([])
    for j in range(w):
        d[i].append(0)

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    d[x-1][y-1] = 1
for i in range(h):
    for j in range(w):
        print(d[i][j], end = " ")
    print()
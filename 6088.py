a, d, n = map(int, input().split())
r = 0
for i in range(n):
    if (i == 0):
        r = a
    else:
        r = r + d
print(r)
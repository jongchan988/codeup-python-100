a, m, d, n = map(int, input().split())
result = 0
for i in range(n):
    if (i == 0):
        result = a
    else:
       result = result * m + d
print(result)
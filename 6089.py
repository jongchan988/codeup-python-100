a, r, n = map(int, input().split())
result = 0
for i in range(n):
    if (i == 0):
        result = a
    else:
       result = result * r
print(result)
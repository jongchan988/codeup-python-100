a, b, c = map(int, input().split())
i = 1
while not (i % a == 0 and i % b == 0 and i % c == 0):
    i += 1
print(i)
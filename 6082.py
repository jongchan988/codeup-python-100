n = int(input())

for i in range(1, n+1) :
    isPrint = True
    word = ''
    if int(i/10) % 10 == 3 or int(i/10) % 10 == 6 or int(i/10) % 10 == 9:
        word += "X"
        isPrint = False
    if i%10==3 or i%10==6 or i%10==9:
        word += "X"
        isPrint = False
    if isPrint:
        word = i
    print(word , end=' ')
    
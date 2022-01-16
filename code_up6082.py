i = int(input())
for a in range(i+1):
    if a % 10 == 3 or a % 10 == 6 or a % 10 == 9:
        print('X',end=' ')
        continue
    print(a,end=' ')
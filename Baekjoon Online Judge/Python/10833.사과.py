
a = int(input())
total = 0
for i in range(0, a):
    b = list(map(int, input().split(" ")))
    temp = int(b[1] / b[0])
    if temp == 0:
        total += b[1]
    else:
        total += b[1] - (b[0] * temp)

print(total)
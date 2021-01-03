minVal = 0
minVal2 = 0
for i in range(0, 5):
    a = int(input())
    if i < 3:
        if minVal == 0:
            minVal = a
        elif minVal > a:
            minVal = a
    else:
        if minVal2 == 0:
            minVal2 = a
        elif minVal2 > a:
            minVal2 = a

print(minVal+minVal2-50)
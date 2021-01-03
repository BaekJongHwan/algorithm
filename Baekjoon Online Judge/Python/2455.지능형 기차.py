total = 0
totalMax = 0
for i in range(0, 4):
    arr = list(map(int, input().split(" ")))
    total -= arr[0]
    total += arr[1]
    if totalMax == 0:
        totalMax = total
    elif totalMax < total:
        totalMax = total

print(totalMax)
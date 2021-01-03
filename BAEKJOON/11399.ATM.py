a = input()
arrTemp = list(map(int, input().split(" ")))
arrTemp.sort()

ll = len(arrTemp)
total = 0

for i in range(0, ll):
    for j in range(0, i+1):
        total += arrTemp[j]

print(total)
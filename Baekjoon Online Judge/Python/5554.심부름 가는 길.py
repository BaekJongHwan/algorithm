
m = 0
for i in range(0, 4):
    m += int(input())

a = m / 60

if a == 0:
    print(0)
    print(m)
else:
    print(int(a))
    print(m-(int(a)*60))
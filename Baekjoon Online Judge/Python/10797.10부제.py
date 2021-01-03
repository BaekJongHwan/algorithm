d = int(input())
car = list(map(int, input().split(" ")))

cnt = 0
for i in car:
    if d == i:
        cnt += 1

print(cnt)
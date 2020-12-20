if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    i=0
    first = 0
    max = 0
    next = 0
    cnt = 0
    for i in arr:
        if n == cnt or cnt > 10 or n < 2:
            break
        if first == 0 and i<=100 and i>=-100:
            max = i
            first = 1
           # print("[1]max:"+str(max))
        elif max < i and max != i and i<=100 and i>=-100:
            next = max
            max = i
            first = 2
           # print("[2]next:" + str(next))
           # print("[2]max:" + str(max))
        elif next < i and max != i and i<=100 and i>=-100:
            next = i
            first = 2
           # print("[3]next:" + str(next))
        elif first == 1 and max != i and i<=100 and i>=-100:
            next = i
            first = 2
           # print("[4]next:"+str(next))

        cnt += 1
    if n <= 10 and n >=2:
        print(next)

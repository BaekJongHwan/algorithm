if __name__ == '__main__':

    n = int(input())
    column, row = n, 2
    arr = [[0]*row for i in range(column)]
    cnt = 0
    tempS1 = []
    tempS2 = []
    s1 = 0
    s2 = 0
    for i in arr:
        if n < 2 or n > 5 or cnt == 5:
            break
        name = input()
        score = float(input())
        arr[cnt][0] = name
        arr[cnt][1] = score
        if s1 == 0:
            s1 = score
            tempS1.append(name)
        #    print("[1]:"+str(tempS1))
        elif s1 == score:
            tempS1.append(name)
        #    print("[2]:" + str(tempS1))
        elif s1 > score:
            s2 = s1
            tempS2 = tempS1.copy()
            s1 = score
            tempS1.clear()
            tempS1.append(name)
        #    print("[3]s1:" + str(tempS1))
        #    print("[3]s2:" + str(tempS2))
        elif s2 == 0 and s1 != score:
            s2 = score
            tempS2.append(name)
        #    print("[5]s1:" + str(tempS1))
        #    print("[5]s2:" + str(tempS2))
        elif s2 > score:
            s2 = score
            tempS2.clear()
            tempS2.append(name)
        #    print("[4]s1:" + str(tempS1))
        #    print("[4]s2:" + str(tempS2))
        elif s2 == score:
            tempS2.append(name)


        cnt += 1

   # print(arr)
   # print(tempS1)
    c = 0
    tempS2.sort()
    if n >= 2 and n <= 5:
        for j in tempS2:
            print(tempS2[c])
            c += 1
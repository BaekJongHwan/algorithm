if __name__ == '__main__':
    n = int(input())
    
    temp = 1
    s = ""
    while temp <= n:
        s = s + str(temp)
        temp = temp + 1
        
    print(s)

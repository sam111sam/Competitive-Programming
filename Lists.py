if __name__ == '__main__':
    N = int(input())
    list = []
    listn = []
    for i in range(N):
        list.append([])
    for i in range(N):
        list[i] = input().split()
    for i in range(N):
        if (list[i][0] == "insert"):
            listn.insert(int(list[i][1]),int(list[i][2]))
        elif (list[i][0] == "print"):
            print(listn)
        elif (list[i][0] == "remove"):
            listn.remove(int(list[i][1]))
        elif (list[i][0] == "append"):
            listn.append(int(list[i][1]))
        elif (list[i][0] == "sort"):
            listn.sort()
        elif (list[i][0] == "pop"):
            listn.pop()
        elif (list[i][0] == "reverse"):
            listn.reverse()
        
        

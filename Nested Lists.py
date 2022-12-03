if __name__ == '__main__':
    list = []
    num = int(input()) 
    for i in range(num):
        list.append([])
    for a in range(num):
        for j in range(2):
            if (j ==1):
                score = float(input())
                list[a].append(score)
            else:
                list[a].append(input())
    for b in range(num):
            store = list[b][0]
            list[b][0]= list[b][1]
            list[b][1] = store
    list.sort()
    
    for y in range(num):
            if (list[0][0] != list[y][0]):
                    global backup 
                    backup = list[y][0]
                    break
    for y in range(num):
            if (list[y][0] == backup ):
                print(list[y][1])
    

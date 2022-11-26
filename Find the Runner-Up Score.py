if __name__ == '__main__':
    n = int(input())
    list=[]
    score = input().split()
    for i in range(n):
        list.append(score[i])
    res = [eval(i) for i in list]
    
    res.sort()
    for i in range(n-1,0,-1):
        if res[i] != res[i-1]:
            print(res[i-1])
            break

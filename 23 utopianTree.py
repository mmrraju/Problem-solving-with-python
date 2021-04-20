for i in range(int(input())):
    n = int(input())
    k = 1
    for i in range(1, n+1):
        if i%2 == 0:
            k +=1 
        else:
            k *=2
    print(k)

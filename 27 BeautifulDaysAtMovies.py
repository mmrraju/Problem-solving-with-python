ijk = input().split()
i = int(ijk[0])
j = int(ijk[1])
m = int(ijk[2])

result = 0 
for i in range(i, j+1):
    try: 
        rev_i = 0
        k = i
        while k>0:
            rem_num = k %10
            rev_i = rev_i*10 + rem_num
            k = k//10
        if abs((i - rev_i))%m == 0:
            result +=1 
    except Exception as e:
        print(e)
print(result)

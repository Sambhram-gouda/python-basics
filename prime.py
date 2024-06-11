num=int(input("Enter the numbers"))

for j in range(2,num+1):
    for i in range(2,j):
        if (j%i==0):
            flag=0
            break
        else:
            flag=1
        if flag==1:
            print(j, end=' ')
            break


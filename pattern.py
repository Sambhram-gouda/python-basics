rows = int(input("Enter X Pattern Odd Rows = "))

print("X Star Pattern")

for i in range(rows):
    for j in range(rows):
        if(i == j or j == rows - 1 - i):
            print('*', end = '')
        else:
            print(' ', end = '')
    print()
def matrix_input():#Retrun a list with 2 demensions.
    nm_str=input("Please input row and col of the matrix with Space between them. Press Enter to end.\n")
    n=int(nm_str.split(' ')[0])
    m=int(nm_str.split(' ')[1])
    numbers_str=input("Please input data with Space between them. Press Enter to end.\n")
    numbers=[]
    for i in range(n*m):
        numbers.append(int(numbers_str.split(' ')[i]))
    pack=[numbers[x:x+m] for x in range(0,n*m,m)]
    return pack
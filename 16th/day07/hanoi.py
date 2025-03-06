def move(n,A,B,C):
    if n == 0:
        return 
    move(n-1,A,C,B)
    print("{}->{}".format(A,C))
    move(n-1,B,A,C)

n = int(input())
move(n,'A','B','C')
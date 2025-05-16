n=int(input("enter n="))
for c1 in range(1,n+1,3):
    print(c1)
    for c2 in range(2,n+1,3):
        print(c2,end="")
        for c3 in range(3,n+1,3):
            print(c3,end="")

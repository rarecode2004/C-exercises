x=[]
n=int(input("enter size="))
for i in range(n):
    x.append(int(input("enter elements=")))
for i in range(n):
    for j in range(n):
        c=x[i]+j
        print(c,end=" ")
    print()

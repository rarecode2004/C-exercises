n=int(input("enter no of terms="))
a=0
b=1
i=1
while (i<n+1):
    print(a)
    c=a+b
    a=b
    b=c
    i+=1

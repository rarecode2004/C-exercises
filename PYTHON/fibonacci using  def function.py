def fibonacci(n):
    a=0
    b=1
    i=1
    for i in range(1,n+1):
        print(a)
        c=a+b
        a=b
        b=c
n=int(input("enter the no of terms="))
fibonacci(n)

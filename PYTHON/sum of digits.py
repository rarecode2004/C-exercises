n=int(input("enter n="))
sum=0
while n>0:
    dig=n%10
    sum=sum+dig
    n=n//10
print("the sum of digits=",sum)

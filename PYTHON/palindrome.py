n=int(input("enter n="))
ans=0
temp=n
while(n>0):
    dig=n%10
    ans=(ans*10)+dig
    n=n//10
if (temp==ans):
    print("palindrome")
else:
    print("not palindrome")

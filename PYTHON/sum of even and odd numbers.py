#GET THE INPUT FROM USER AND PRINT THE SUM OF EVEN AND ODD NUMBERS:

n=int(input("enter the number="))
even=0
odd=0
for i in range(1,n+1):
    if (i%2==0):
        even=even+i
    else:
        odd=odd+i
print("the sum of even nos is=",even)
print("the sum of odd nos is =",odd)
    

n1=int(input("enter n1="))
n2=int(input("enter n2="))
print(n1+n2)
hcf=1
for i in range(2,(n1+n2)):
    if(n1%i==0)and (n2%i==0):
        hcf=i
print("the hcf is=",hcf)

# chef categorizes instagram account as spam,if following account(x) is more than 10 times the count of followers(y)
# the condition is ==> (x>(10*y))

a=int(input("enter size="))
for i in range(a):
    x=int(input("enter x="))
    y=int(input("enter y="))
    if (x>(10*y)):
        print("yes")
    else:
        print("no")

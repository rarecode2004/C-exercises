def isort():
    for i in range(len(list)):
        temp=list[i]
        
        j=i-1
        while(j>=0):
            if(temp<list[j]):
                list[j+1]=list[j]
                list[j]=temp
                j=j-1
            else:
                break
list=[1,5,4,3,2]
isort()
print(list)

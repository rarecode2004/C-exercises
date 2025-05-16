def bubblesort():
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
list=[3,2,6,5,4,8]
bubblesort()
print(list)

        
                

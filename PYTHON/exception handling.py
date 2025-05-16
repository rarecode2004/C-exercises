# if the file not created in notepad and , if we use write mode => it automatically creates the file in notepad.
'''try:
    a=open("sample.txt","w")
    a.write("hello")
    a=open("sample.txt","r")
    print(a.read())
except:
    print("file not created")'''

#output is "hello"






#if the file not created in notepad and,if we use read mode => it  will throw to the except part and print the statement.

try:
    a=open("sample.txt","r")
    a.write("hi")
except FileNotFoundError as e:
    print(e)
except IOError:
    print("input output error")
    
#if I use the created text,the output is "input output error".
#if I use the not created text (i.e).excel.txt ,the output is "FileNotFoundError"





    





    

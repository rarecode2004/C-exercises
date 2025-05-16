try:
    list=[]
    n=int(input("enter size="))
    for i in range(n):
        list.append(int(input("enter elements=")))
    print(list)
except ValueError:
    print("value error")
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)
except StringError as e:
    print(e)
except SpecialCharacterError as e:
    print(e)
finally:
    print("execution over")

#program to print multiplication table rerpeatedly
a=int(input("enter the number for which u want tables"))
while (a!=0):
    for x in range(1,11):
        print(x,"*",a,"=",x*a)
    a=int(input("enter 0 to quit or any number to continue"))

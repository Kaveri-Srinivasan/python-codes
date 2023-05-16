#program to find odd,even,max,min,pos,neg after entering 0
count=1
sum=0
positivenum=0
negativenum=0
odd=0
even=0
max=0
min=0
while count <=10:
    num=int(input("enter the number"))
    if num>0:
        positivenum+=1
        sum+=num
    elif num<0:
        negativenum+=1
        sum+=num
    if num%2==0:
        even+=1
    elif num%2!=0:
        odd+=1
    if num>max:
        max=num
    elif num<min:
        min=num
    else:
        print("total sum is:",sum)
        print("positive num is:",positivenum)
        print("negative num is:",negativenum)
        print("even numbers is:",even)
        print("odd num is:",odd)
        print("maximum num is:",max)
        print("minimum is:",min)
        break

    
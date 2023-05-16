num = int(input("Enter a number ( greater than 1)"))  
i = 2
while i <= num / 2:
    if num % i == 0:
        print("The entered number is a PRIME number")
    i=i+1
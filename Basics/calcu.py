a=input("Enter Number 1:")
b=input("Enter Number 2:")
c=input("Choose your operator:\n 1.+ \n 2.- \n 3.* \n 4./ ",)

if c == "1":
    res=a+b
elif c == "2":
    res=a-b
elif c == "3":
    res=a*b
elif c=="4":
    if b==0:
        print("Division by zero")
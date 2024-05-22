print("Odd or Even")
number=int(input("Enter the number to evaluate whether it is odd or even: "))
if number%2 == 1:
    print(number, "is odd.")
elif number%2 == 0:
    print(number, "is even.")
else:
    print(number, "is neither.")

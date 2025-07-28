print("Input two numbers and an operator (e.g +, -, / and *) to explore this basic calculator")
num1 = eval(input("Enter your first number : "))
num2 = eval(input("Enter your second number : "))
ch = input("Enter any of these operators [+, -, / or *] ")
if ch == "/":
        if num2 < 1:
            print ("The denominator must be greater than zero")
        else:
            print("The division of the two numbers is", num1/num2)
elif ch =="+":
    print("The sum of the two numbers is", num1+num2)
    
elif ch == "-":
    print("The difference between the two numbers is", num1-num2)
    
elif ch =="*":
    print("The product of the two numbers is", num1*num2)
else:
    print("Enter an appropriate operator")
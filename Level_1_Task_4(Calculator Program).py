# Calculator Program

num1 = float(input("\nEnter First Number : "))
num2 = float(input("\nEnter Second Number : "))

operation = input("\nEnter the Operator (+, -, *, /, %) : ")

if operation == "+":
    print("\n", num1,"+",num2,"=", num1+num2) # For Addition

elif operation == "-":
    print("\n", num1,"-",num2,"=", num1-num2) # For Subtraction

elif operation == "*":
    print("\n", num1,"*",num2,"=", num1*num2) # For Multiplication

elif operation == "/":
    print("\n", num1,"/",num2,"=", num1/num2) # For Division

elif operation == "%":
    print("\n", num1,"%",num2,"=", num1%num2) # For Modulus

else:
    print("\nInvalid Operation")
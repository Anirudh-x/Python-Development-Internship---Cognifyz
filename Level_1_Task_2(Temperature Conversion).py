# Temperature Conversion

temp = float(input("\nEnter a Temperature Value : "))
unit = input("Enter the Unit of Measurement (C for Celsius & F for Fahrenheit): ")
print("\n")

if unit.lower() == "c":
    f = temp *(9/5) + 32 # It will convert Celsius in Fahrenheit by using formula F = C * (9/5) + 32
    print(f"Temperature in Fahrenheit : {f} F\n")

elif unit.lower() == "f":
    c = (temp - 32) * 5/9 # It will convert Fahrenheit in Celsius by using formula C = (F - 32) * 5/9
    print(f"Temperature in Celsius : {c} C\n")

else:
    print("Invalid Unit !!!")
# Fibonacci Sequence

def fibonacci(num):
    a = 0
    b = 1

    if num == 1:
        print(a)

    elif num <= 0:
        print("Invalid Integer")

    else:
        print(f"{a}\n{b}")
        for i in range(2,num):
            c = a + b
            a = b
            b = c
            print(c)

input_num = int(input("\nEnter an Integer : "))
fib = fibonacci(input_num)
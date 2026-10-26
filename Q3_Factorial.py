n = int(input("Enter a number: "))
if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    factorial = 1
    i = n
    while i > 1:
        factorial *= i
        i -= 1
    print(f"Factorial of {n} is {factorial}")

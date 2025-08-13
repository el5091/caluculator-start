def add(x, y):
      return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y

print("select operation")
print("1.Add")
print("2.Sub")
print("3.Mul")
print("4.Div")

while True:
    choice = input("Enter choice (1/2/3/4): ")
    if choice in ("1", "2", "3", "4"):
          try:
              num1 = float(input("Enter first number: "))
              num2 = float(input("Enter second number: "))
              result = add(num1, num2)
              print(result)
              if choice == "1":
                  print(num1, "+", num2, "=", result)

              elif choice == "2":
                  print(num1, "-", num2, "=", result)

              elif choice == "3":
                  print(num1, "*", num2, "=", result)

              elif choice == "4":
                  print(num1, "/", num2, "=", result)


print(next_calculation:= input("Enter next calculation (y/n): " ))
if next_calculation == "y":
 choice = input("enter choice (1/2/3/4): ")
if next_calculation != "n": exit()



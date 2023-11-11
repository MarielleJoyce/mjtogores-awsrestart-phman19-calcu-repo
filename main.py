def add(x, y):
  return x + y
def substract(x, y):
  return x - y
def multiply(x, y):
  return x * y
def divide(x, y):
  return x / y
no1 = eval(input("Enter the first number: "))
no2 = eval(input("Enter the second number: "))
print("select the option")
print("1. Sum")
print("2. Sub")
print("3. MUL")
print("4. DIV")
print("5. EXIT")
while True:
  choice = int(input("Enter the choice from the above options: "))
  if choice in (1, 2, 3, 4, 5):
    if choice == 1:
      print("Sum of two numbers", no1, "and ", no2, "is:", add(no1, no2))
    elif choice == 2:
      print("Subtract of two numbers", no1, "and ", no2, "is:", substract(no1, no2))
    elif choice == 3:
      print("Multiplication of two numbers", no1, "and ", no2, "is:", multiply(no1, no2))
    elif choice == 4:
      print("Division of two numbers", no1, "and ", no2, "is:", divide(no1, no2))
    elif choice == 5:
     print("Will exit. Thank you!")
     exit(0)
  else:
    print("Invalid choice. Please try again")
def add(x, y):
  return x + y
def subtraction(x, y):
  return x - y
def multiply(x, y):
  return x * y
def divide(x, y):
  return x / y
no1 = eval(input("Enter the First Number:"))
no2 = eval(input("Enter the Second Number:"))
print("Select the operation:")
print("1. SUM")
print("2. SUB")
print("3. MUL")
print("4. DIV")
print("5. Exit")
while True:
  choice = int(input("Enter the choice from the above:"))
  if choice in (1, 2, 3, 4, 5):
      if choice == 1:
          print("Sum of two numbers", no1, "and", no2, "is:", add(no1, no2))
      elif choice == 2:
          print("Subtract of two numbers", no1, "and", no2, "is:", subtraction(no1, no2))
      elif choice == 3:
          print("Multiply of two numbers", no1, "and", no2, "is:", multiply(no1, no2))
      elif choice == 4:
          print("Division of two numbers", no1, "and", no2, "is:", divide(no1, no2))
      elif choice == 5:
          print("Will exit. thank you")
          break
  else:
      print("Invalid choice. Please try again")